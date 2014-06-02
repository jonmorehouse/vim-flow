import os
import glob
import imp
import flowconfig

# whether or not to always reload from source
ignore_cache = True
cache = {}

# list of paths to read modules from
modulePaths = [os.path.join(os.path.dirname(__file__), "../flows")]
if flowconfig.flow_path:
    modulePaths.append(flowconfig.flow_path)

def modules():

    global use_cache
    for modulePath in modulePaths:
        for filepath in glob.glob("%s/*py" % modulePath):
            
            # get module_name
            module_name = os.path.splitext(os.path.basename(filepath))[0]

            # now check to see if it needs to be loaded
            if not cache.get(module_name) or ignore_cache:
                cache[module_name] = imp.load_source(module_name, filepath)

    # now return the module_cache (dicts are passed by reference)
    return cache

