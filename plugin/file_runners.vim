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
""" Python Project Runners
"""
function File_Runners#PythonRunner(target)

    if isdirectory(a:target) && exists("g:runCommand")
        :call Utilities#CleanShell(g:runCommand)
    " this is just a file - call the single file method
    elseif filereadable(a:target)
        :call Utilities#CleanShell("python ". a:target)
    endif

endfunction

function File_Runners#PythonTestRunner(target)
    
    if isdirectory(a:target)
        :call Utilities#CleanShell("cd ". g:basePath, "source bin/activate", "\./bin/nosetests --nocapture")
    elseif ! a:target =~ "_test.py" 
        let file=substitute(a:target, ".py", "_test.py", "")
        :call Utilities#CleanShell("cd ". g:basePath, "source bin/activate", "\./bin/nosetests --nocapture ". file)
    else
        :call Utilities#CleanShell("cd ". g:basePath, "source bin/activate", "\./bin/nosetests --nocapture ". a:target)
    endif
endfunction

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
    let command="docker run -i -t ". tag ." /bin/bash" 
    if exists("g:dockerRunCommand")
        let command=g:dockerRunCommand
    endif
    " now call the correct command
    :call CleanShell(command)
endfunction

function File_Runners#DockerfileTestRunner(...)
    " initialize the tag needed
    let tag="test"
    if exists("g:dockerTag")
        tag=g:dockerTag
    endif
    let command="docker build -t ". tag ." ."
    :call CleanShell(command)
endfunction

"""
""" Ruby Project Runners
"""
function File_Runners#RubyRunner(target)

    if isdirectory(a:target) && exists("g:runCommand")
        :call Utilities#CleanShell("cd ". g:basePath, g:runCommand)
    else
        :call Utilities#CleanShell("ruby ". a:target)
    endif
endfunction

function File_Runners#RubyTestRunner(target)
    
    " check rake tasks to see if tests exists
    " some ideas could be - look into rake 
    " look for a .cucumber file
    " look for a spec file

endfunction


"""
""" Cucumber Project Runners
"""
function File_Runners#CucumberRunner(target)
    echo a:target
    " build entire project as needed
    if isdirectory(a:target)
        :call Utilities#CleanShell("cd ". g:basePath, "cucumber")
    else
        " need to find this exact path
        :call Utilities#CleanShell("cd ". g:basePath, "cucumber ". a:target)
    endif
endfunction

function File_Runners#CucumberTestRunner(target)
    :call File_Runners#CucumberRunner(a:target)
endfunction

"""
""" Coffeescript/Node Project Runners
"""
function File_Runners#CoffeeRunner(target)

    :call Utilities#CleanShell("coffee ". a:target)

endfunction

function File_Runners#JavascriptRunner(target)
    
    :call Utilities#CleanShell("node ". a:target)

endfunction

"""
""" Haskell
"""
function File_Runners#HaskellRunner(target)
    :call Utilities#CleanShell("runghc ". @%)
endfunction

