import flowtils

filenames = ["Cakefile"]
extension = ["sample_ext"]

def test(**kwargs):

    flowtils.vim_shell("make bash do something", clean = False)

def run(**kwargs):

    flowtils.tmux_shell("echo HERE && echo TEST")





