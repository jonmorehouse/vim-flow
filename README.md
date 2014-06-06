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

" run alt command for this module
:FlowAlt

" run a command in the tmux window
:FlowMux

" lock/unlock a file, so you can edit other files while still running flows on this file
:FlowLock

" toggle whether or not to run flow commands in tmux or from within vim
:FlowToggleTmux
~~~

## Configuration

Prefix all commands with clear
~~~ vim
let g:flow_clean = 1
~~~

Send commands to tmux instead of executing from within vim
~~~ vim
" you can use tmux, vim or python to run command in a new pane, within vim or silently
let g:flow_runtime = tmux 
~~~

By default, tmux commands will run in a split window in the current tmux session. You can optionally specify a different pane or session to send commands to.
~~~ vim
let g:flow_tmux_session = "some_session_name"
let g:flow_tmux_pane = 2
~~~

Some power users may want to build their own flows to override the built in ones. By specifying a `g:flow_path` you can add a directory of your own flows.
~~~ vim
let g:flow_path = $HOME."/.flows"
~~~

## Flow Flags

You can add flags to any file as you are developing, or to a project as a whole by adding a `.flowfile` with flags.

~~~ bash
# .flowfile

# set what command should be run
#flow-command: ls
#flow-setup: clear
#flow-teardown: echo FINISHED
#flow-runtime: tmux 

~~~


## Hacking

Contributions welcome. There's an endless amount of flows to be built out, from cucumber flows to docker flows. I'll be implementing them as I come across them in my own work. Open issues and fork away!


