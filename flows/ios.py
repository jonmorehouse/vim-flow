import flowtils as u

extensions = ["h", "m"]

def run(**kw):

    if u.execute_project_file(**kw):
        return
    
    command = u.basepath_command("xctool build", **kw)
    u.tmux_shell(command, **kw)


