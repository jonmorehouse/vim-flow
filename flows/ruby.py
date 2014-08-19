import flowtils as u
import vim
import re

filenames = ["Rakefile"]
extensions = ["rb"]

def rubymotion(command):

    u.python_shell("tmux split-window -t temp")
    u.tmux_shell("tmux kill-pane -t 0 && %s " % command, session = "temp", pane = 1)

def get_rubymotion_test_command(**kw):
    if u.has_file(kw, ".rubymotion"):
        with open(u.base_filepath(".rubymotion", **kw)) as f:
            lines = f.readlines()
            if len(lines) > 0:
                return lines[0].strip()
            
    return "bundle exec rake spec"
    
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
        print get_rubymotion_test_command(**kw)
        return rubymotion(get_rubymotion_test_command(**kw))

    # run the applicatin in the simulator
    u.shell("bundle exec rake", **kw)

