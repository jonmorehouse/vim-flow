"check to see if argv was passed
"resolve argv to grab the base directory
"grab the current working directory
function Runner#BasePath()
	if exists("g:basePath")
		return
	endif
	let g:basePath=system("pwd")
endfunction

function Runner#Shell()
 
endfunction

