import flowtils as u
import vim
import re

filenames = ["Cakefile"]
extensions = ["coffee"]

def run(**kwargs):

    # write all vim buffers - force write, and then open the current path again
    vim.command(":wall")

    if re.match(r'.*_spec.coffee$', kwargs.get("filepath")):
        command="cd %s && jasmine-node --coffee %s" % (kwargs.get("basepath"), kwargs.get("filepath"))
    elif u.has_file(kwargs, "Cakefile"):
        command = "cake test"
    else:
        command = "coffee %s" % kwargs.get("filepath")

    # run the command in the shell with the given user preferences
    u.shell(command)

