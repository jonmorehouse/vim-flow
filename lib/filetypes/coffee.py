import flowtils as u
import vim

filenames = ["Cakefile"]
extensions = ["coffee"]

def run(**kwargs):

    # write all vim buffers - force write, and then open the current path again
    vim.command(":wall")
    if u.has_file(kwargs, "Cakefile"):
        command = "cake test"
    else:
        command = "coffee %s" % kwargs.get("filepath")
    # run the command in the shell with the given user preferences
    u.shell(command)

