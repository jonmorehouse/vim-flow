import os.path
import yaml


def get_defs(filepath):
    '''get_flow_defs: returns the best matched flowfile and returns the flow_defs

    This method walks directories from the current filepath all the way to `/`
    and will return the first `.flow.yml` file it finds.

    '''
    dirpath = os.path.dirname(filepath)
    flow_filepath = None
    while dirpath != '/':
        flow_filepath = os.path.join(dirpath, '.flow.yml')
        if os.path.exists(flow_filepath):
            break
        dirpath = os.path.abspath(os.path.join(dirpath, '../'))
    else:
        print 'No `.flow.yml` found...'
        return None

    try:
        with open(flow_filepath, 'r') as fh:
            flow_defs = yaml.safe_load(fh)
    except IOError:
        print '`flow.yml` file at %s appears to be non-readable from within vim' % flow_filepath
    except yaml.YAMLError:
        print '`flow.yml` file at %s is not parseable yaml' % flow_filepath
    else:
        return flow_defs

    return None


def _format_cmd_def(cmd_def, filepath):
    '''_format_cmd_def: format a command def
    
    * template `filepath` into the cmd string
    * add the runner field 
    '''
    templates = {
        '{{filepath}}': filepath,
    }
    for keyword, value in templates.iteritems():
        cmd_def['cmd'] = cmd_def['cmd'].replace(keyword, value)
    cmd_def['cmd'] = cmd_def['cmd'].strip()

    if 'tmux_session' in cmd_def:
        cmd_def['tmux_pane'] = cmd_def.get('tmux_pane', 0)
        cmd_def['runner'] = 'tmux'
    else:
        cmd_def['runner'] = 'vim'

    return cmd_def


def get_cmd_def(filepath, flow_defs):
    '''find_cmd: returns a cmd_def based upon the flow_defs and filepath

    return {
        'runner': 'string | vim|tmux',
        'tmux_sesion': 'string |  tmux_session',
        'tmux_pane': 'int | tmux_pane',
        'cmd': 'string, command to be executed',
    }
    '''
    basename = os.path.basename(filepath)
    filename, ext = basename.split('.', 1)

    cmd_def = flow_defs.get('all')
    if ext in flow_defs:
        cmd_def = flow_defs[ext]

    if cmd_def is None:
        print 'no valid command definitions found in `.flow.yml`. Try adding an extension or `all` def...'
        return None
    
    return _format_cmd_def(cmd_def, filepath)
