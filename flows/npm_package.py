import flowtils as u
import vim

filenames = ["package.json"]

def test(**kwargs):
    u.close_tmux()


def run(**kwargs):

    command = "cd %s && npm install" % kwargs.get("basepath")
    # always open in tmux shell
    u.tmux_shell(command)

