"""
""" Go Project runners
"""
function File_Runners#GoRunner(target)

    " run the project
    if isdirectory(a:target)
        " find the root main.go file
        let file=substitute(system("find ". g:basePath ." -type f -name \"*main.go\""), "\n", "", "")
        :call Utilities#CleanShell("go run ". file)
    " if this is a test file - redirect to the test caller
    elseif a:target =~ "_test.go"
        :call File_Runners#GoTestRunner(a:target)
    " if it doesn't look like a file - then go ahead and try to call the
    " correct file as needed
    else 
        :call Utilities#CleanShell("go run ". a:target)
    endif

endfunction

function File_Runners#GoTestRunner(target)
    
    " check to see if any go test flags are set ...
    let flags=""
    if exists("g:goTestFlags")
        let flags = g:goTestFlags 
    endif

    " test the current package
    if isdirectory(a:target)
        :call Utilities#CleanShell("go test ". flags ." .")
    " this looks like a normal test file
    elseif a:target =~ "_test.go"
        :call Utilities#CleanShell("go test ". flags ." ". a:target)
    " attempt to try the test version of this file
    else 
        let file=substitute(a:target, ".go", "_test.go", "")
        :call Utilities#CleanShell("go test ". flags ." ". file)
    endif
endfunction

"""
""" Ruby Project Runners
"""

"""
""" Python Project Runners
"""

"""
""" Docker Project Runners
"""
function File_Runners#DockerfileRunner(...)

    " initialize the tag needed
    let tag="test"
    if exists("g:dockerTag")
        tag=g:dockerTag
    endif
    " initialize the run command
    let run="docker run -i -t ". tag ." /bin/bash" 
    if exists("g:dockerRunCommand")
        let run=g:dockerRunCommand
    endif
    " now call the correct command
    
endfunction

function File_Runners#DockerfileTestRunner(...)
        
endfunction

"""
""" Ruby Project Runners
"""

"""
""" 
"""










