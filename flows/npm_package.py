import flowtils as u
import vim

filenames = ["package.json"]

def install(**kw):

    vim.command("let package=input(\"Enter package name: \")")
    package = vim.eval("package")
    command = "npm install %s" % package
    u.shell(command, **kw)

def run(**kw):

    command = "cd %s && npm install" % kw.get("basepath")
    # always open in tmux shell
    u.tmux_shell(command, **kw)

