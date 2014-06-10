import flowtils as u

extensions = ["go"]

def run(**kw):

    command = "go run %s" % kw.get("filepath")
    u.shell(command, **kw)
    

