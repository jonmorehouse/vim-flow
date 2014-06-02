if exists("g:vim_flow_load") || &cp
  finish
endif
let g:vim_flow_loaded = 1

" make sure that vim is compiled with correct python2.7 suppor
if !has("python")
  echo "vim-flow requires python support"
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

import flow

def flow_reload():
  imp.reload(flow)
EOF

" reload vim-flow
command! Flow :python flow.run()
command! FlowTest :python flow.test()
" toggle lock on / off for current file
command! FlowLock :python flow.lock()
command! FlowReload :python flow_reload()
command! -nargs=1 FlowMux python flow.tmux('<args>')

