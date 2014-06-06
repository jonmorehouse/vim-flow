import os
import flowtils as u

def has_command(**kw):

    flowfile = u.get_flowfile(**kw)
    if not flowfile:
        return False

    # grab flags from file
    flags = u.get_flags(**flowfile)

    if flags.get("command"):
        return True
    return False

def run(**kw):

    flags = u.get_flags(**u.get_flowfile(**kw))
    u.shell(flags.get("command"), **kw)


