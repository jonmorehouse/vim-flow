import os
import subprocess as s
import re

try:
    import vim
except:
    vim = None

attr_cache = {}

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
    attr["relative_filepath"] = re.sub(r'^/', "", filepath.replace(basepath, ""))
    attr["git"] = git
    attr["repo"] = False # functionality added later
    attr["ext"] = extension if extension else False
    attr["extension"] = attr["ext"]

    return attr

# run with the correct defaults
def shell(command, **kwargs):

    if flowconfig.use_tmux:
        tmux_shell(command, **kwargs)
    else:
        vim_shell(command, **kwargs)

def python_shell(command):

    # run the command and grab stderr/stdout to check if git repo or not
    output = s.Popen(command, shell=True, stdout=s.PIPE, stderr=s.PIPE)
    stdout, stderr = output.communicate()
    return stderr, stdout

def vim_shell(command, **kwargs):

    if kwargs.get("clean") and kwargs.get("clean") is True or flowconfig.clean:
        command = "printf \"\033c\" && %s" % command
    vim.command("! %s" % command)

def tmux_shell(command, retry_allowed = True, **kwargs):

    # make sure clean is not requested
    if kwargs.get("clean") and kwargs.get("clean") is True or flowconfig.clean:
        command = "clear && %s" % command

    # tmux send -t session.0 (just assume window 0) for now
    # window's don't really make sense here because you never would be able to see 2 different windows in a tmux session at once
    full_command = "tmux send -t %s.%s \"%s\" ENTER" % (flowconfig.tmux_session, flowconfig.tmux_pane, command)
    stderr, stdout = python_shell(full_command) 

    # if stderr, there was most likely no tmux window available. Try to create one
    if stderr and retry_allowed:
        stderr, stdout = python_shell("tmux split-window -hd")
        # normalize windows in case there was a vertical split, switch to a horizontal split
        if not stderr:
            vim.command("call feedkeys(\"\<C-W>K\")")
        tmux_shell(command, False)
    elif stderr:
        print "Unable to send command to tmux %s.%s. Please make sure this pane exists." % (flowconfig.tmux_session, flowconfig.tmux_pane)

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

def close_tmux():

    python_shell("tmux kill-pane -t %s.%s" % (flowconfig.tmux_session, flowconfig.tmux_pane))
    vim.command("call feedkeys(\"\<C-W>H\")")


import flowconfig
