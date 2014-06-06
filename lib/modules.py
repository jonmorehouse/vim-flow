import os
import glob
import imp
import flowconfig

# whether or not to always reload from source
ignore_cache = True
cache = {}

base_dir = os.path.join(os.path.dirname(__file__))
# list of paths to read modules from
module_paths = [os.path.abspath(os.path.join(base_dir, "../flows"))]
if flowconfig.flow_path:
    module_paths.append(flowconfig.flow_path)

def get_module(module_name, filepath, **kw):
    return imp.load_source(module_name, filepath)

def modules():

    global use_cache
    for modulePath in module_paths:
        for filepath in glob.glob("%s/*py" % modulePath):
            
            # get module_name
            module_name = os.path.splitext(os.path.basename(filepath))[0]

            # now check to see if it needs to be loaded
            if not cache.get(module_name) or ignore_cache:
                cache[module_name] = get_module(module_name, filepath)

    # now return the module_cache (dicts are passed by reference)
    return cache

