"check to see if argv was passed
"resolve argv to grab the base directory
"grab the current working directory
fu! Utilities#BasePath()
    if exists("g:basePath")
        return
    endif
    let g:basePath=substitute(system("pwd"), "\n", "","")
endfunction

" local.vimrc override!
fu! Utilities#LoadLocalVimrc()
    call Utilities#BasePath()   
    let localPath = g:basePath ."/.local.vimrc"
    if filereadable(localPath)
        execute("so ". localPath)
    endif
endfunction

" run a command in a clean shell
fu! Utilities#CleanShell(...)
    " execute a single command
    fu! ExecuteCommand(command)
        execute "! ". a:command
    endfunction
    " always clear the screen before executing anything
    let command="printf \"\033c\"" 
    " now loop through each of the commands and append them
    let c=1
    while c <= a:0
        let commandPiece=eval("a:". c)
        let command=command ." && ". commandPiece
        let c += 1
    endwhile
    " now execute our fully formed command
    call ExecuteCommand(command)
endfunction

fu! Utilities#Zsh(...)
    let command = "source ~/.zshrc && "
    let c=1
    while c <= a:0
        let commandPiece=eval("a:". c)
        let command=command ." ". commandPiece
        let c += 1
    endwhile
    execute "! ". command
endfunction

fu! Utilities#CleanZsh(...)
    let command="printf \"\033c\" && source ~/.zshrc &&" 
    let c=1
    while c <= a:0
        let commandPiece=eval("a:". c)
        let command=command ." ". commandPiece
        let c += 1
    endwhile
    execute "! ". command
endfunction


fu! Utilities#GetFileType(path)
    return &ft
endfunction

fu! Utilities#Capitalize(input)
    return substitute(a:input, '.', '\u&', '') 
    "return join([toupper(a:input[0]), a:input[1:len(a:input)]], "")
endfunction
