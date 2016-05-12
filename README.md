# Vim Flow

VimFlow allows you to run commands as part of your vim workflow.

## flow.yml files

`VimFlow` is a small utility for parsing a local `.flow.yml` file which allows
you to define different "actions" to take for a specific file. The `flow` file syntax supports localized commands (commands that will run in your vim session) as well as background commands with tmux (commands that are sent to a specified tmux session,pane combination).

Given the following `.flow.yml`:

```yaml
---
# specify a default command that will be run for all files in a project that don't match an extension
all:
  # clear the vim window before running any sort of command
  cmd: clear; echo "hi"

# run a command for python files
py: 
  tmux_session: work
  tmux_pane: 1
  # run a command in another tmux window 
  cmd: |
    curl -vvv https://

```


## Usage


* `:FlowRun`

## Installation




## FAQ 


