"check to see if argv was passed
"resolve argv to grab the base directory
"grab the current working directory
function Utilities#BasePath()
	if exists("g:basePath")
		return
	endif
	let g:basePath=substitute(system("pwd"), "\n", "","")
endfunction

" local.vimrc override!
function Utilities#LoadLocalVimrc()
	let localPath = g:basePath ."/.local.vimrc"
	if filereadable(localPath)
		:so .local.vimrc
	endif
endfunction

" run a command in a clean shell
function Utilities#CleanShell(...)
	" execute a single command
	function ExecuteCommand(command)
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

function Utilities#GetFileType(path)
	return &ft
endfunction


