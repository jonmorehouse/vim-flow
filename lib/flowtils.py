import os
import subprocess as s
import re
import glob

try:
    import vim
except:
    vim = None

attr_cache = {}

# check whether or not to force use vim / tmux etc
def get_flags(**kw):

    filepath = kw.get("filepath")
    flags = {}

    if os.path.isdir(filepath):
        return flags

    with open(filepath, "r") as f:

        for line in f.readlines():

            mg = re.match("^#flow-(?P<flag>.*): (?P<value>.*)$", line)
            if not mg:
                continue
            # possibly do some other stuff
            flags[mg.group("flag")] = mg.group("value")

    return flags

def get_file(kw, filepath):

    filepath = os.path.join(kw.get("basepath"), filepath)
    if os.path.isfile(filepath):
        with open(filepath) as f:
            return f.read()
    return False

def git_basepath(filepath): 

    filedir = os.path.dirname(filepath) 
    # should return the basepath of the currently executing file
    command = "cd %s && git rev-parse --show-toplevel" % filedir
    stderr, stdout = python_shell(command)
    # return true and gitdir if its a git repo!
    if stdout: 
        return stdout.strip(), True
    return filedir, False

def get_path_attributes(filepath): 

    global attr_cache 
    if attr_cache.has_key(filepath):
        return attr_cache.get(filepath)

    basepath, git = git_basepath(filepath)
    basename = os.path.basename(filepath)
    extension = os.path.splitext(basename)[1].lstrip(".")
    
    # return file attributes here
    attr = {}
    attr["filepath"] = filepath # full path for execution
    attr["basepath"] = basepath # base directory
    attr["filename"] = basename 
    attr["basename"] = basename
    attr["directory_name"] = basepath.split("/")[-1]
    attr["relative_filepath"] = re.sub(r'^/', "", filepath.replace(basepath, ""))
    attr["git"] = git
    attr["repo"] = False # functionality added later
    attr["ext"] = extension if extension else False
    attr["extension"] = attr["ext"]

    return attr

def modify_command_with_hooks(command, **kw):

    flags_list = [get_flags(**kw)]
    flowfile = get_flowfile(**kw)
    setup = teardown = None

    if flowfile:
        flags_list.append(get_flags(**flowfile))

    # grab the flags and set teardown/setup properly
    for flags in flags_list:
        if flags.get("setup"):
            setup = flags.get("setup")
        if flags.get("teardown"):
            teardown = flags.get("teardown")

    # add in suffix/prefixes for the command
    if setup:
        command = "%s && %s" % (setup, command)
    if teardown:
        command = "%s && %s" % (command, teardown)

    return command

# run with the correct defaults
def shell(command, **kw):

    flags = {}
    if kw.get("filepath"):
        flags = get_flags(**kw)

    # initialize runtime
    if flags.get("runtime"):
        runtime = flags.get("runtime")
    elif kw.get("runtime"):
        runtime = kw.get("runtime")
    else:
        runtime = flowconfig.runtime
    
    # add setup/teardown methods to command
    command = modify_command_with_hooks(command, **kw)
     
    # now call correct runtime functions
    if runtime == "tmux":
        tmux_shell(command, **kw)
    elif runtime == "python":
        python_shell(command, **kw)
    else:
        vim_shell(command, **kw)

def python_shell(command, **kw):

    # run the command and grab stderr/stdout to check if git repo or not
    output = s.Popen(command, shell=True, stdout=s.PIPE, stderr=s.PIPE)
    stdout, stderr = output.communicate()
    return stderr, stdout

def vim_shell(command, **kw):

    if kw.get("clean") and kw.get("clean") is True or flowconfig.clean:
        command = "printf \"\033c\" && %s" % command
    vim.command("! %s" % command)

def tmux_shell(command, **kw):

    # make sure clean is not requested
    if not "clear" in kw.keys():
        command = "clear && %s" % command

    session = kw.get("session") if kw.get("session") else flowconfig.tmux_session
    # pane can oftentimes be zero
    pane = kw.get("pane") if "pane" in kw.keys() else flowconfig.tmux_pane

    # tmux send -t session.0 (just assume window 0) for now
    # window's don't really make sense here because you never would be able to see 2 different windows in a tmux session at once
    full_command = "tmux send -t %s.%s \"%s\" ENTER" % (session, pane, escape_command(command))
    stderr, stdout = python_shell(full_command) 

    # if stderr, there was most likely no tmux window available. Try to create one
    if stderr and not "no_retry_allowed" in kw:
        stderr, stdout = python_shell("tmux split-window -hd -t %s" % session)
        # normalize windows in case there was a vertical split, switch to a horizontal split
        if not stderr:
            vim.command("call feedkeys(\"\<C-W>K\")")
        tmux_shell(command, no_retry_allowed = False, **kw)
    elif stderr:
        print "Unable to send command to tmux %s.%s. Please make sure this pane exists." % (session, pane)

# get the value of a vim variable if it exists
def vim_variable(name):

    if int(vim.eval("exists(\"%s\")" % name)):
        return vim.eval(name)

    return False

# whether or not a project has a file
def has_file(basepath, filename):

    if type(basepath) == dict:
        basepath = basepath.get("basepath")
    if os.path.isfile(os.path.join(basepath, filename)):
        return True
    return False

def base_filepath(name, **kw):

    return os.path.join(kw.get("basepath"), name)

def close_tmux():

    python_shell("tmux kill-pane -t %s.%s" % (flowconfig.tmux_session, flowconfig.tmux_pane))
    vim.command("call feedkeys(\"\<C-W>H\")")

def escape_command(command):

    chars = ["$"]

    for char in chars:
        command = re.sub(r"\$", "\\$", command)

    return command

def vim_echo(msg):

    vim.command("! echo %s" % msg)

def get_flowfile(**kw):

    os.chdir(kw.get("basepath"))
    files = glob.glob(".flowfile")
    if len(files) < 1: 
        return False

    return get_path_attributes(files[-1])

def execute_project_file(**kw):
    contents = get_file(kw, ".project")
    if not contents: return False
    tmux_shell(contents, session = "temp", pane = 0)
    return True
        
import flowconfig
