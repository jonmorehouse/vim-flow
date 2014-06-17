import flowtils as u

filenames = ["Gemfile", "Gemfile.lock"]

def run(**kw):

    command = "bundle"
    u.shell(command, **kw)

def test(**kw):

    command = "bundle"
    u.tmux_shell(command, **kw)
