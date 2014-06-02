import flowtils as u

filenames = ["package.json"]

def test(**kwargs):

    command = "jsonlint %s" % kwargs.get("filepath")
    u.shell(command)

def run(**kwargs):

    command = "cd %s && npm install" % kwargs.get("basepath")
    # always open in tmux shell
    u.tmux_shell(command)

