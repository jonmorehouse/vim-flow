Vim Runner
==========

Notes / Thoughts
----------------

* every time buffers are created / switched, we need to call the BootstrapFile method
  * configure test / run scripts
  * configure the current file variable
  * ensure the basePath elements and leader mappings are correctly configured
* implement vimunit 

Usage
-----

```
# install via bundler
git submodule add git@github.com:jonmorehouse/vim-runner.git bundle/vim-runner

# in your vimrc
call Runner#Bootstrap()

```

Public Functions
----------------

* TestRunner()
  * mapped to <Leader>rt
  * run project tests
  * look for g:testCommand || best guess based on project type
* FileRunner()
  * if in a test type of file 
  * otherwise try to run the current file
* CleanShell()
  * run a command in a clean shell

Private Methods
---------------

* getFileType() - return filetype as needed
* getRunType() - single test / run. Project test / run
* TestFile()
* TestProject()
* RunProject()
* RunFile()

