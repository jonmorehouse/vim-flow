import flowtils as u
import vim
import re

filenames = ["Cakefile"]
extensions = ["coffee"]

def run(**kw):

    # write all vim buffers - force write, and then open the current path again
    vim.command(":wall")

    if re.match(r'.*_spec.coffee$', kw.get("filepath")):
        command="cd %s && cake -p %s test" % (kw.get("basepath"), kw.get("filepath"))
    elif u.has_file(kw, "Cakefile"):
        command = "cd %s && cake test" % kw.get("basepath")
    else:
        command = "coffee %s" % kw.get("filepath")

    # run the command in the shell with the given user preferences
    u.shell(command, **kw)

