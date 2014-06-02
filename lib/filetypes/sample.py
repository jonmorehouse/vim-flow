import flowtils

filenames = ["sample_file"]
extension = ["sample_ext"]

def test(**kwargs):

    flowtils.vim_shell("make bash do something", clean = False)

def run(**kwargs):

    flowtils.vim_shell("")
    

