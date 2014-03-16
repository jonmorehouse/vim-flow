Vim Runner
==========

Public Functions
----------------

* GetBasePath()
  * set the base path of the project
  * parse any argv commands that were passed 
* ProjectRunner()
  * mapped to <Leader>rp
  * run base command for project
  * look for g:runCommand || best guess based on filetype
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


