Vim Runner
==========

ToDo
----

* add in more base project types
* move all file runners into their own directory with each being its own file
* show options / create help command

Installation
-----

```
cd ~/dotfiles/vim # or wherever vim configuration is

# install via bundler
git submodule add git@github.com:jonmorehouse/vim-runner.git bundle/vim-runner

```
General Usage
-------------

```
# attempt to run current file
<Leader>rr

# attempt to test current file
<Leader>rt

# attempt to test project
<Leader>rtp

# attempt to run project
<Leader>rp
```

GoLang Usage
------------

```
# .local.vimrc
# set specific test flags (optional)
let g:goTestFlags="-vvv"

# main.go

# run the current file
<Leader>rr 

# run the current project - looks for the root/main.go file
<Leader>rp

# run tests on the current file
<Leader>rt

# test current package
<Leader>rtp

```

Dockerfile Usage
----------------

```
# .local.vimrc
# set specific tag to use for this build (optional, default is test)
let g:dockerTag=""

# set specific run command (optional, default is to shell in)
let g:dockerRun=""

# Dockerfile

# run the current dockerfile
<Leader>rr
<Leader>rp

# test the current docker file
<Leader>rt
<Leader>rtp

```

Cucumber Usage
--------------

```
# run current spec
<Leader>rr
<Leader>rt

# run all specs
<Leader>rp
<Leader>rtp

```


