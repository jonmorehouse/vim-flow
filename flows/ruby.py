import flowtils as u
import vim
import re

filenames = ["Rakefile", "Gemfile", "Gemfile.lock"]
extensions = ["rb"]

def run(**kw):

    # run tests by default ... this shouldn't be that slow (hopefully)
    u.shell("rake test", **kw)
    
def test(**kw):

    # run the applicatin in the simulator
    u.tmux_shell("rake")

