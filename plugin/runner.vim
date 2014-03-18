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
    " bootstrap test mappings
    call TestMapper(type)
    " bootstrap run mapping
    call RunMapper(type)
    " now that we have mapped the commands, call the local vimrc to ensure
    " that no re-mapping occurs
    call Utilities#LoadLocalVimrc()
endfunction

" link up autocommands as needed
au BufNewFile,BufRead * call Runner#BootstrapFile()
" now lets actually call the global vimrc file at all times
autocmd VimEnter * call Runner#Bootstrap()

"""
""" PRIVATE METHODS
"""
" now configure the leader mappings as needed
function TestMapper(type)
    call Utilities#BasePath()
    let functionName="File_Runners#". a:type ."TestRunner"
    if exists("*".functionName)
        " bootstrap the file command
        let fileCommand=":call ". functionName ."(\"". @% ."\")"
        :execute("map<Leader>rt ". fileCommand ."<CR>")
        " bootstrap the project command
        let projectCommand=":call ". functionName ."(\"". g:basePath ."\")"
        :execute("map<Leader>rtp ". projectCommand ."<CR>")
    endif
endfunction

" initialize run commands
function RunMapper(type)
    call Utilities#BasePath()
    let functionName="File_Runners#". a:type ."Runner"
    if exists("*". functionName)
        " bootstrap the file command
        let fileCommand=":call ". functionName ."(\"". @% ."\")"
        :execute("map<Leader>rr ". fileCommand ."<CR>")
        " bootstrap the project command
        let projectCommand=":call ". functionName ."(\"". g:basePath ."\")"
        :execute("map<Leader>rp ". projectCommand ."<CR>")
    endif
endfunction


