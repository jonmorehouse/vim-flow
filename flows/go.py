import flowtils as u

extensions = ["go"]

def run(**kw):

    project_file_contents = u.get_file(kw, ".project")
    if project_file_contents:
        u.tmux_shell("cd %s; %s" % (kw.get("basepath"), project_file_contents), session = "temp", pane = 0)
        return

    command = "go run %s" % kw.get("filepath")
    u.shell(command, **kw)
    

