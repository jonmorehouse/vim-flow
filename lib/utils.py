import os
import subprocess as s

try:
    import vim
except:
    vim = None

attr_cache = {}

def git_basepath(filepath): 

    filedir = os.path.dirname(filepath) 
    # should return the basepath of the currently executing file
    command = "cd %s && git rev-parse --show-toplevel" % filedir

    # run the command and grab stderr/stdout to check if git repo or not
    output = s.Popen(command, shell=True, stdout=s.PIPE, stderr=s.PIPE)
    stdout, stderr = output.communicate()

    # return true and gitdir if its a git repo!
    if stdout: 
        return stdout, True
    return filedir, False

def run_command(command_string, clean = True):

    # generate shell command and run from within vim
    pass

def get_path_attributes(filepath): 

    global attr_cache 
    if attr_cache.has_key(filepath):
        return attr_cache.get(filepath)

    basepath, git = git_basepath(filepath)
    basename = os.path.basename(filepath)
    extension = os.path.splitext(basename)[1]
    
    # return file attributes here
    attr = {}
    attr["filepath"] = filepath # full path for execution
    attr["basepath"] = basepath # base directory
    attr["filename"] = basename 
    attr["basename"] = basename
    attr["relative_filepath"] = filepath.replace(basepath, "")
    attr["git"] = git
    attr["repo"] = False # functionality added later
    attr["ext"] = extension if extension else False
    attr["extension"] = attr["ext"]

    return attr


