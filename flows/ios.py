import flowtils as u

extensions = ["h", "m"]

def run(**kw):

    project_file = u.get_file(kw, ".project")
    if project_file:
        u.python_shell("tmux split-window -t temp")
        u.tmux_shell("tmux kill-pane -t 0 && %s " % project_file, session = "temp", pane = 1)
        return
    
    command = u.basepath_command("xctool build", **kw)
    u.tmux_shell(command, **kw)


