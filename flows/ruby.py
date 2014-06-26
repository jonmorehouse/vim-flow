import flowtils as u
import vim
import re

filenames = ["Rakefile"]
extensions = ["rb"]


def run(**kw):
    if u.has_file(kw, ".rubymotion"):
        u.tmux_shell("quit", clear = False, session = "rubymotion", pane = 0)
        u.tmux_shell("bundle exec rake spec", clear = False, session = "rubymotion", pane = 0)
        return

    if u.has_file(kw, "Rakefile"):
        command = "bundle exec rake spec"
    else:
        command = "ruby %s" % kw.get("filepath")

    # run tests by default ... this shouldn't be that slow (hopefully)
    u.shell(command, **kw)
    
def test(**kw):

    if u.has_file(kw, ".rubymotion"):
        u.tmux_shell("quit", clear = False, session = "rubymotion", pane = 0)
        u.tmux_shell("bundle exec rake", clear = False, session = "rubymotion", pane = 0)
        return

    # run the applicatin in the simulator
    u.shell("bundle exec rake", **kw)

