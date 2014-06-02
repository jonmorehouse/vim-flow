import vim
import flowtils
import os
import imp
import glob
import modules

filelock = None

def run():
    _run("run")

def test():
    _run("test")

def lock():
    
    global filelock
    if not filelock:
        filelock = _get_file_path()
        print "File locked"
    else:
        filelock = None
        print "File unlocked"


def _run(method = "run"):

    # generate file information to be passed around as kwargs
    filepath = _get_file_path()
    attrs = flowtils.get_path_attributes(filepath)

    # find the correct module 
    module = _get_module(attrs.get("filename"), attrs.get("extension"))

    if not module or not hasattr(module, method):
        print "No module available for this filepath"
        return

    # call method
    getattr(module, method)(**attrs)
    
def _get_file_path():

    global filelock
    if filelock:
        return filelock
    return vim.current.buffer.name

def _get_module(filename, extension):

    # check all modules
    for module_name, module in modules.modules().iteritems():
        # check against extension
        if extension and extension in module.extensions:
            return module
        # check if its a registered filename, for instance Gemfile or Rakefile (ruby)
        if filename in module.filenames:
            return module

    return None


