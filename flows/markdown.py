import flowtils as u
import webbrowser

filenames = [".idea"]
extensions = ["md"]

def test(**kwargs):

    u.close_tmux()

def run(**kwargs):

    # run server in tmux window 
    u.tmux_shell("grip %s" % kwargs.get("filepath"))

    # open file in your browser of choice
    webbrowser.open("http://localhost:5000")



