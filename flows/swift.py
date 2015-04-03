import flowtils as u
import vim
import re

extensions = ["swift"]

def run(**kw):
    project_file_contents = u.get_file(kw, ".project")
    if project_file_contents:
        u.tmux_shell(project_file_contents, session = "temp", pane = 0)
        return
