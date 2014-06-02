import flowtils as u
import vim

extensions = ["vim"]

def run(**kwargs):

    vim.command(":bufdo :w | :b %s" % kwargs.get("filepath"))
    vim.command(":so %s" % kwargs.get("filepath"))
    

