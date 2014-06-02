import flowtils as u
import vim

extensions = ["vim"]

def run(**kwargs):

    vim.command(":wall")
    vim.command(":so %s" % kwargs.get("filepath"))

