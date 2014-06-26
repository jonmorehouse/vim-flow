import flowtils as u
import vim
import re

filenames = ["Rakefile"]
extensions = ["rb"]

def rubymotion(command):

    u.python_shell("tmux split-window -t rubymotion")
    u.tmux_shell("tmux kill-pane -t 0 && %s " % command, session = "rubymotion", pane = 1)

def run(**kw):
    if u.has_file(kw, ".rubymotion"):
        rubymotion("bundle exec rake")
        return

    if u.has_file(kw, "Rakefile"):
        command = "bundle exec rake spec"
    else:
        command = "ruby %s" % kw.get("filepath")

    # run tests by default ... this shouldn't be that slow (hopefully)
    u.shell(command, **kw)
    
def test(**kw):

    if u.has_file(kw, ".rubymotion"):
        rubymotion("bundle exec rake spec")
        return

    # run the applicatin in the simulator
    u.shell("bundle exec rake", **kw)

