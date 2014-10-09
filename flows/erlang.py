import flowtils as u
import vim

extensions = ["erl"]

def run(**kw):
    if u.execute_project_file(**kw):
        return
    u.basepath_command("rebar compile eunit", tmux = True, **kw)



