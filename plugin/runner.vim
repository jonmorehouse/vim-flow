" Bootstrap the plugin
function Runner#Bootstrap()
    " make sure to bootstrap the basePath as needed
    call Utilities#BasePath()
    " now load up local vimrc files
    call Utilities#LoadLocalVimrc()
    " open up explore if no args are passed on startup
    if len(argv()) == 0 
        Explore
    " check to make sure directory wasn't passed
    elseif isdirectory(argv()[0])
        let g:basePath=argv()[0]
        Explore
    endif
endfunction

" bootstrap a new buffer / autocommand etc
function Runner#BootstrapFile()
    let type=Utilities#Capitalize(Utilities#GetFileType(@%))
    if !exists("g:fileLock") || g:fileLock != "true"
        " bootstrap test mappings
        call TestMapper(type)
        " bootstrap run mapping
        call RunMapper(type)
        " now that we have mapped the commands, call the local vimrc to ensure
        " that no re-mapping occurs
        call Utilities#LoadLocalVimrc()
    endif
endfunction

function Runner#BootstrapCurrentFile()
    " remove lock
    let g:fileLock="false"
    " bootstrap the current file
    :call Runner#BootstrapFile()
    " lock again
    let g:fileLock="true"
endfunction

function Runner#ToggleFileLock()

    if !exists("g:fileLock")
        let g:fileLock="true"
    endif
    if g:fileLock == "true"
        let g:fileLock="false"
    else
        let g:fileLock="true"
    endif
    echo "g:fileLock = ". g:fileLock

endfunction

"""
""" Autocommand Event Mappings
"""
" link up autocommands as needed
" :help autocmd-events
au BufNewFile,BufRead,BufEnter,BufWinEnter * call Runner#BootstrapFile()
" now lets actually call the global vimrc file at all times
autocmd VimEnter * call Runner#Bootstrap()

"""
""" LEADER MAPPINGS
"""
map<Leader>ll :call Runner#BootstrapCurrentFile()<CR>
map<Leader>lu :call Runner#ToggleFileLock()<CR>

"""
""" PRIVATE METHODS
"""
" now configure the leader mappings as needed
function TestMapper(type)
    :call Utilities#BasePath()
    let functionName="File_Runners#". a:type ."TestRunner"
    let path=expand('%:p') 

    if exists("*".functionName)
        " bootstrap the file command
        let fileCommand=":call ". functionName ."(\"". path ."\")"
        :execute("map<Leader>rt ". fileCommand ."<CR>")
        " bootstrap the project command
        let projectCommand=":call ". functionName ."(\"". g:basePath ."\")"
        :execute("map<Leader>rtp ". projectCommand ."<CR>")
    endif
endfunction

" initialize run commands
function RunMapper(type)
    :call Utilities#BasePath()
    let functionName="File_Runners#". a:type ."Runner"
    let path=expand('%:p') 
    if exists("*". functionName)
        " bootstrap the file command
        let fileCommand=":call ". functionName ."(\"". path ."\")"
        :execute("map<Leader>rr ". fileCommand ."<CR>")
        " bootstrap the project command
        let projectCommand=":call ". functionName ."(\"". g:basePath ."\")"
        :execute("map<Leader>rp ". projectCommand ."<CR>")
    endif
endfunction


