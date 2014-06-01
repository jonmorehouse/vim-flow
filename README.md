# Vim Runner
> A framework for developing with vim. Smartly execute files / projects from your current vim session with one key press

## Assumptions / Rules

1. All executions are based upon the current filepath
  * this filepath can be locked
  * checks for git root - run's project settings
  * single file fallback
2. Two entry points - Test/Run. These will often be the same





## Development Notes

* utilities
  * identify git path from path
  * get file extension

~~~ python.py 

filenames = [Fabfile]
extensions = []

~~~

~~~ ruby.py

extensions = [ ]
filenames = [ ]

test(basepath, filepath):

run(basepath, filepath):


~~~




