import vim
import os

import flow
import runners

lock_cache = {}

def run_flow(cache=lock_cache):
    '''flow: run a flow for the current filepath

    * find and load flow defs
    * build cmd_def
    * run cmd_def
    '''
    if 'filepath' in lock_cache:
        filepath = lock_cache['filepath']
    else:
        filepath = _get_filepath()
    flow_defs = flow.get_defs(filepath)
    if flow_defs is None:
        return

    cmd_def = flow.get_cmd_def(filepath, flow_defs)
    if cmd_def is None:
        return

    runner = {
        'vim': runners.vim_runner,
        'tmux': runners.tmux_runner,
        'sync-remote': runners.sync_remote_runner,
        'async-remote': runners.async_remote_runner,
    }[cmd_def['runner']]

    runner(cmd_def)

def toggle_lock(cache=lock_cache):
    if 'filepath' in cache:
        del cache['filepath']
        print("file lock released...")
    else:
        cache['filepath'] = _get_filepath()
        print("file lock set...")

def _get_filepath():
    return vim.current.buffer.name
