import vim
import os
import flowtils

# clean
clean = flowtils.vim_variable("g:flow_clean")
if str(clean) == "1" or str(clean) == "true":
    clean = True
else:
    clean = False

# set use_tmux
use_tmux = flowtils.vim_variable("g:flow_use_tmux")
if str(use_tmux) == "1":
    use_tmux = True
else:
    use_tmux = False

# set tmux_pane
tmux_pane = flowtils.vim_variable("g:flow_tmux_pane")
if not tmux_pane:
    # set it from command line
    stderr, stdout = flowtils.python_shell("tmux display-message -p \"#P\"")
    if stderr:
        use_tmux = False
    try:
        tmux_pane = int(stdout) + 1
    except e:
        use_tmux = False
else:
    tmux_pane = int(tmux_pane)

# set tmux_session
tmux_session = flowtils.vim_variable("g:flow_tmux_session")
if not tmux_session:
    # set from current session
    stderr, stdout = flowtils.python_shell("tmux display-message -p \"#S\"")
    if stderr:
        use_tmux = False
    tmux_session = stdout.strip()

# set additional flow directory - this is for custom functionality
flow_path = flowtils.vim_variable("g:flow_path")



