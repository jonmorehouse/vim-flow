import flowtils as u

extensions = ["gemspec"]

def run(**kw):

    command = "gem build %s" % kw.get("filepath")
    u.shell(command, **kw)



