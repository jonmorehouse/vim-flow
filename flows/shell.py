import re
import flowtils as u
import os
from stat import *

def has_shebang(filepath):
    
    with open(filepath, 'r') as f:
        first_line = f.readline()

    # check shebang exists
    if not re.match(r'^#.*', first_line):
        return False
    return True

def run(**kw):

    # check permissions
    stat = os.stat(kw.get("filepath"))
    
    # make sure permissions are set
    u.python_shell("if [[ ! -x %s ]];then chmod +x %s; fi" % (kw.get("filepath"), kw.get("filepath")))

    # now execute the filepath
    u.shell(kw.get("filepath"))

