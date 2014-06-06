import flowtils as u
import vim

extensions = ["py"]

def run(**kw):

    vim.command(":wall") 
    
    if u.has_file(kw, "Fabfile.py"):
        command = "cd %s && fab test" % kw.get("basepath")
    else:
        command = "python %s" % kw.get("filepath")

    u.shell(command, **kw)

