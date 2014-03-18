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
	let type=Utilities#GetFileType(@%)
	" initialize loops to map files to the correct filetypes
	if type ==# "go" 
		let testCommand="File_Runners#GoTest"
		let runCommand="File_Runners#GoRun"
	elseif type ==# "python"
		let testCommand="File_Runners#PythonTest"
		let runCommand="File_Runners#PythonRunner"
	elseif type ==# "js""
		let testCommand="File_Runners#JavascriptTest"
		let runCommand="File_Runners#JavascriptRunner"
	elseif type ==# "ruby"
		let testCommand="File_Runners#RubyTest"
		let runCommand="File_Runners#RubyRunner"
	elseif type ==# "cucumber"
		let testCommand="File_Runners#CucumberRunner"
		let runCommand="File_Runners#CucumberRunner"
	elseif type ==# "docker"
		let testCommand="File_Runners#DockerBuilder"
		let runCommand="File_Runners#DockerRunner"
	endif
	
	" now configure the leader mappings as needed
	if exists("testCommand")
		" run current tests
		map<Leader>rt execute()<CR>
		" run all tests
		map<Leader>rtp execute()<CR>
	endif
	" initialize run commands
	if exists("runCommand")
		" run current file
		map<Leader>rr execute()<CR>
		" run current project
		map<Leader>rp execute()<CR>
	endif
endfunction

