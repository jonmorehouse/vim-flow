import flowtils as u
import vim

filenames = ["Cakefile"]
extensions = ["coffee"]

def run(**kwargs):

    # write all vim buffers
    vim.command(":bufdo :w")
    if u.has_file(kwargs, "Cakefile"):
        command = "cake test"
    else:
        command = "ls && coffee %s" % kwargs.get("filepath")
    # run the command in the shell with the given user preferences
    u.shell(command)

