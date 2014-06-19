import flowtils as u
import vim
import re

filenames = ["Rakefile"]
extensions = ["rb"]


def run(**kw):

    if u.has_file(kw, "Rakefile"):
        command = "bundle exec rake spec"
    else:
        command = "ruby %s" % kw.get("filepath")

    # run tests by default ... this shouldn't be that slow (hopefully)
    u.shell(command, **kw)
    
def test(**kw):

    # run the applicatin in the simulator
    u.tmux_shell("bundle exec rake")

