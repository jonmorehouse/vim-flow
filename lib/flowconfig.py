import vim
import os
import flowtils

variables = [("g:flow_use_tmux", False), ("g:flow_use_tmux", False), ("g:flow_tmux_session", True)]

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
    tmux_pane = int(stdout) + 1
else:
    tmux_pane = int(tmux_pane)

# set tmux window

# set tmux_session
tmux_session = flowtils.vim_variable("g:flow_tmux_session")
if not tmux_session:
    # set from current session
    stderr, stdout = flowtils.python_shell("tmux display-message -p \"#S\"")
    if stderr:
        use_tmux = False
    tmux_session = stdout.strip()

