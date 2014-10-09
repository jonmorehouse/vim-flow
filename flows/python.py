import flowtils as u
import vim

extensions = ["py", "hs"]

def run(**kw):

    vim.command(":wall") 
    
    project_file_contents = u.get_file(kw, ".project")
    if project_file_contents:
        u.tmux_shell(project_file_contents, session = "temp", pane = 0)
        return

    if u.has_file(kw, "Fabfile.py"):
        command = "cd %s && fab test" % kw.get("basepath")
    else:
        command = "python %s" % kw.get("filepath")

    u.shell(command, **kw)

