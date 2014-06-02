import flowtils

filenames = ["Cakefile"]
extension = ["sample_ext"]

def test(**kwargs):

    flowtils.shell("make bash do something", clean = True)

def run(**kwargs):

    flowtils.shell("echo HERE && echo TEST", clean = True)





