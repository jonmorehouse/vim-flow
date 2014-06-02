import flowtils as u
import vim

filenames = ["package.json"]

def install(**kwargs):

    vim.command("let package=input(\"Enter package name: \")")
    package = vim.eval("package")
    command = "npm install %s" % package
    u.shell(command)

def run(**kwargs):

    command = "cd %s && npm install" % kwargs.get("basepath")
    # always open in tmux shell
    u.tmux_shell(command)

