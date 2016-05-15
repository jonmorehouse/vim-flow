import contextlib
import os
import subprocess
import stat
import tempfile
import vim


def _build_script(cmd_def):
    '''_build_script: in order to simplify things such as escaping and
    multiline commands, we template out all `cmds` into a script that is
    written to a tempfile and executed
    ''' 
    fh, filepath = tempfile.mkstemp()

    # if the script doesn't start with a hashbang, then we default to the local $SHELL var
    if not cmd_def['cmd'].startswith('#!'):
        hashbang = '#!{}'.format(os.environ.get('SHELL', '/usr/bin/env bash'))
        os.write(fh, hashbang)
        os.write(fh, '\n')
    os.write(fh, cmd_def['cmd'])
    os.write(fh, '\n')

    # ensure that the filepath is executable by the runner process, the default
    # tempfile is 0600 
    os.chmod(filepath, 0777)
    return filepath


def _cleanup_script(filepath):
    '''_cleanup_script: remove the temp file
    '''
    # os.remove(filepath)
    pass


@contextlib.contextmanager
def _script(cmd_def):
    '''_script: a context manager for creating a command script and cleaning it up

    usage:
        with _script(cmd_def) as script_filepath:
            print script_filepath
    '''
    filepath = _build_script(cmd_def)
    yield filepath
    _cleanup_script(filepath)


def vim_runner(cmd_def):
    '''vim_runner: run a command in the vim tty
    '''
    with _script(cmd_def) as script_path:
        vim.command('! {}'.format(script_path))


def tmux_runner(cmd_def):
    '''tmux_runner: accept a command definition and then run it as a shell script in the tmux session.pane.
    '''
    with _script(cmd_def) as script:
        args = ['tmux', 
                'send', 
                '-t', 
                '%s.%s' % (cmd_def['tmux_session'], cmd_def['tmux_pane']), 
                'sh -c \'%s\'' % script, 
                'ENTER']

        env = os.environ.copy()
        process = subprocess.Popen(args, env=env)
        process.wait()
