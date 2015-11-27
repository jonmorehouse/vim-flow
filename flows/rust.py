import flowtils as u

extensions = ["rs"]

def run(**kw):
    project_file_contents = u.get_file(kw, ".project")
    if project_file_contents:
        u.tmux_shell("cd %s; %s" % (kw.get("basepath"), project_file_contents), session = "temp", pane = 0)
        return

    output_file = kw.get("filepath").split(".rs")[0]
    command = "rustc %s; %s" % (kw.get("filepath"), output_file)
    u.shell(command, **kw)
