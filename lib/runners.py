import os
import subprocess
import vim

def vim_runner(cmd_def):
    vim_cmd = '! {}'.format(cmd_def['cmd'])
    vim.command(vim_cmd)


def tmux_runner(cmd_def):
    '''tmux_runner: accept a command definition and run a shell command that
    sends the command to the correspondant tmux window.

    eg:
        #.flow.yml
        ---
        all: 
            tmux_session: temp
            tmux_pane: 1
            cmd: clear && echo "hello"

    would be processed as: 
        tmux send -t temp.0 \'echo "hello"\' ENTER
    '''
    tmux_cmd = 'tmux send -t {session}.{pane} \'{cmd}\' ENTER'.format(
        session=cmd_def['tmux_session'],
        pane=cmd_def['tmux_pane'],
        cmd=cmd_def['cmd'],
    )

    cmd = ['tmux', 'send', '-t', '%s.%s' % (cmd_def['tmux_session'], cmd_def['tmux_pane']), '%s' % cmd_def['cmd'], 'ENTER']
    env = os.environ.copy()
    process = subprocess.Popen(cmd, env=env)
    process.wait()
