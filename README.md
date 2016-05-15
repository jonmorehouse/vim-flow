# Vim Flow

Declarative build-test-run workflow with Vim.

```yaml
#.flow.yaml
go: 
  cmd: go run {{filepath}}
```

![image](https://cdn.pbrd.co/images/VD58yLW.gif)

VimFlow keeps you in your editor and productive allowing you to run, test or format your current project with a single command. By exposing a simple interface and allowing you to define run commands in whatever shell language you are comfortable with, you can easily configure projects and scripts to your liking.

Some common use cases for vim-flow are:

* running your favorite one off script executor of choice eg: bash|python|ruby|go run etc...
* running a code formatter / test suite for a large project you are working on
* running any arbitrary script at any given time from vim while working

## Flow Run

The `:FlowRun` command is responsible for executing anything and everything for a buffer within vim. Behind the scenes, `:FlowRun` will fetch the current filename and find a `.flow.yml` file to run. `vim-flow` starts at the current buffer's directory and walks upwards looking for the first `.flow.yml` file it finds.

Let's say you are working on `main.go` and have the following directory structure:

```bash
.
├── .flow.yml
└── main.go
```

and your `.flow.yml` file contains the following:

```yaml
# .flow.yml
go: 
  cmd: goimports -w {{filepath}} && go run {{filepath}}

```

`:FlowRun` will load in the local `.flow.yml`, match up and find the script `go imports {{filepath}} && go run {{filepath}}` by extension (.go) and will run that in the current vim window.


`cmd` can be any command you can run in your terminal! Behind the scenes, `vim-flow` templates this out into a temporary file script and runs that script as part of its execution.

Here's a more complicated example:

```bash
.
|-- .flow.yml
|-- benchmark_test.go
└── main.go
```

```yaml
# .flow.yml
go:
  cmd: | #!/bin/bash
    cd $(dirname {{filepath}})
    set -e
    goimports -w .
    go test -v .
    go test -bench=.
    GOOS=linux GOARCH=386 go build server.go
```

Behind the scenes, `flow` would write the entire contents of the `cmd` out to a temporary script and execute it as a bash script. In this particular example, you could run a formatter, test suite, benchmark suite and a build job all with one vim command. 

## Flow Lock

Part of the `flow` workflow is staying in your editor, popping around and changing filepaths frequently. Let's say you are working on a large project with many different files and build jobs:

In this example, you may want to have different flows for the `gopackage` directory, some bash scripts in `/scripts` and even the `bins/main.go` file.

```bash
.
├── .flow.yml
├── bins
│   └── main.go
├── gopackage
│   ├── .flow.yml
│   ├── gopackage.go
│   └── gopackage_test.go
└── scripts
    ├── build
    └── test

```

You may also have an editor open with many of these buffers open. While you are working in `gopackage` you may want to build the entire project. 

`vim-flow` supports the ability to "lock" onto a file. By running `:FlowToggleLock` you can lock onto a file and any future calls to `:FlowRun` will use that file. This allows you to pop around to many different files while still calling the flow that you'd like to.

Let's say we have the following flow, where you want to run `go build` for any go file and simply want to execute any other file by itself.

```bash
default: 
  cmd: {{filepath}}

go: 
  cmd: | #!/bin/bash
    cd $(dirname {{filepath}})
    go build .

```

By locking onto `main.go` with `:FlowToggleLock` in your vim session, whenever you call `:FlowRun` `flow` will run the `go` flow. This allows you to switch to other files, buffers around your work space and still run the flow you'd like.

To unlock a file, simply call `:FlowToggleLock` again.

## Tmux Support

`vim-flow` supports running commands in a separate **tmux** session and pane. For longer builds or when you'd like to avoid interrupting your vim session, you can specify this in a flow file:

```yaml
# .flow.yaml
go:
  tmux_session: foo
  tmux_pane: 1
  cmd: | #!/bin/bash
    echo "executing go script in another tmux pane"
    go run {{filepath}}
```

![tmux example](https://cdn.pbrd.co/images/VFLAzcF.gif)

## Installation

`vim-flow` can be installed by simply adding it as a dependency using `vundle`:

```vim
Plugin 'jonmorehouse/vim-flow'
```

`vim-flow` requires `python` support within vim. If you aren't sure if you have `python` enabled in your current vim installation, the following command will return 1/0 for success failure.

```vim
:echo has('python')
```

## Getting Started

You'll probably want to add some reasonable **flow** defaults. Its nice to be able to hit `:FlowRun` from any sort of "standard" one off script and it _just work_.

Adding a `$HOME/.flow.yml` file with some reasonable defaults is a good starting point.

```yaml
# $HOME/

# execute any plain script by itself
default:
  cmd: {{filepath}}


# run flake8 and python {{filepath}} for any python file
py: 
  cmd: |#!/bin/bash
    flake8 {{filepath}}
    python {{filepath}}

# run go fmt and go run {{filepath}} for any golang file
go: 
  cmd: |#!/bin/bash
    go fmt -w {{filepath}}
    go run {{filepath}}

```

## Customization

VimFlow provides two commands out of the box:

* `:FlowRun` - run a flow for the current file.
* `:FlowToggleLock` - lock or unlock the current file

By design, `vim-flow` doesn't have any opinions about how these commands should be run as part of your vim workflow. For instance, it might be helpful to map one or both of these commands to normal mode mappings to avoid having to call them from the vim command line each time.

For example, to link `<Leader>,` to `:FlowRun` and `<Leader>l` to `:FlowToggleLock`  you can add the following to your `$HOME/.vimrc` file:

```vim
# $HOME/.vimrc
map <Leader>, :FlowRun<CR>
map <Leader>l :FlowToggleLock<CR>
```

## FAQ 

> Why use python instead of entirely native vim-script?

It's definitely possible to write the entirety of this plugin in vimscript, but I've found that it s more intuitive to use python. It's a pretty standard vim dependency and allows for testing (coming soon) and a better maintenance/development experience. The vimscript surface area is super minimal and can be found #[here](https://github.com/jonmorehouse/vim-flow/blob/master/plugin/vim-flow.vim).


> Why not use foo plugin?

Plugins exist for many different runtimes/languages etc in `vim`, but attempting to set up Vim for every unique project is tedious and requires many different plugins. With `vim-flow` you have a common interface to running, testing and developing within a project. 

By using shell script, you can do _more_ things the way you'd like.

> Why a flow file?

Well, yaml is pretty easy to update and it's an interesting idea to create flow files for the projects you work on. In future iterations, we may add support to run flows from outside of vim.

