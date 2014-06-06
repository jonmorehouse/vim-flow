import flowtils as u
import vim
import re

def has_command(**kw):

    flags = u.get_flags(**kw)

    if flags.get("command"):
        return True
    return False

def run(**kw):

    flags = u.get_flags(**kw)
    u.shell(flags.get("command"), **kw)

