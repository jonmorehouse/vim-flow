if exists("g:vim_runner_loaded") || &cp
  finish
endif
let g:vim_runner_loaded = 1

" make sure that vim is compiled with correct python2.7 suppor
if !has("python")
  echo "vim-runner requires python support"
  finish
endif

python <<EOF
from os import path as p
import sys
import vim
import imp

# generate path that needs to 
base_path = p.abspath(p.join(vim.eval("expand('<sfile>:p:h')"), "../lib"))
sys.path.insert(0, base_path)

import runner

def vim_runner_reload():
  imp.reload(runner)
EOF

" reload coad
command! VimRunnerReload :python vim_runner_reload()

