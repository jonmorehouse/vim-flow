import flowtils

filenames = ["sample_filename"]
extension = ["sample_ext"]

def test(**kwargs):

    flowtils.shell("echo TEST", clean = True)

def run(**kwargs):

    flowtils.shell("echo RUN", clean = True)





