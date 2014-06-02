import vim
import os
import flowtils

variables = [("g:flow_use_tmux", False), ("g:flow_use_tmux", False), ("g:flow_tmux_session", True)]

for var in variables:
    check_vim = flowtils.vim_variable(var[0])

    print check_vim




