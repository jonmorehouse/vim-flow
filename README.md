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

## Dependencies

This plugin has a lot of dependencies, based upon the projects you are running. For most cases, you're dependencies will installed already, if not check out the corresponding flow for that filetype. 

That being said, there are a few dependencies specifically designed for flow.
~~~ bash
# github markdown preview server
$ pip install grip 
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
let g:flow_use_tmux = 1
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

## Hacking

Contributions welcome. There's an endless amount of flows to be built out, from cucumber flows to docker flows. I'll be implementing them as I come across them in my own work. Open issues and fork away!


