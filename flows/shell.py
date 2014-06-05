import re
import flowtils as u
import os
from stat import *

def has_shebang(filepath):
    
    # directories don't have shebangs :)
    if os.path.isdir(filepath):
        return False

    with open(filepath, 'r') as f:
        first_line = f.readline()

    # check shebang exists
    if not re.match(r'^#.*', first_line):
        return False
    return True

def get_command(**kw):

    command = kw.get("filepath")

    # first check to see if there is a shebang commands line
    with open(kw.get("filepath"), "r") as f:

        for line in f.readlines()[1:]:
            # attempt to grab matchgroup
            mg = re.match(r"^#flow: (?P<args>.*)$", line) 
            
            # check if args were passed
            if mg and mg.group("args"):
                return "%s %s" % (command, mg.group("args"))

    return command

def run(**kw):

    # check permissions
    stat = os.stat(kw.get("filepath"))
    
    # make sure permissions are set
    u.python_shell("if [[ ! -x %s ]];then chmod +x %s; fi" % (kw.get("filepath"), kw.get("filepath")))

    # get proper command
    command = get_command(**kw)

    u.shell(command)



