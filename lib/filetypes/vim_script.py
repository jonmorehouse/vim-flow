import flowtils as u
import vim

extensions = ["vim"]

def run(**kwargs):

    vim.command(":bufdo :w")
    vim.command(":so %s" % kwargs.get("filepath"))
    

