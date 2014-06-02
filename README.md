# Vim Flow
> A framework for developing from within vim. Execute your project or file from one vim command. 

## Installation

This plugin was built on mac and has only been tested with mac for now. However, assuming your vim was included with python 2.7, you shouldn't have any problems. No external python modules are required.

~~~ vim
" vimrc
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

Plugin 'jonmorehouse/vim-flow'
~~~

## Usage

Vim-Flow is a highly configureable framework that allows you to execute any file you happen to be editing with one command. As this project matures, more filetypes will be supported.

~~~ vim

" execute the current file or project
:Flow

" test the current file or project
:FlowTest

~~~

For now, to add custom functionality, fork the project and add new python files in the lib/filetypes directory.


## Configuration

Prefix all commands with clear
~~~ vim
let g:flow_clean = 1
~~~

Send commands to tmux instead of executing from within vim
~~~ vim
let g:flow_use_tmux = 1
~~~

By default, tmux commands will run in a split window in the current tmux session. You can optionally specify a different pane or session to send commands to.
~~~ vim
let g:flow_tmux_session = "some_session_name"
let g:flow_tmux_pane = 2
~~~

