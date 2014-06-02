import flowtils as u
import vim

print "flow loaded"

extensions = ["py"]

def run(**kwargs):

    vim.command(":wall") 
    
    if u.has_file(kwargs, "Fabfile.py"):
        command = "cd %s && fab test" % kwargs.get("basepath")
    else:
        command = "python %s" % kwargs.get("filepath")

    u.shell(command)

