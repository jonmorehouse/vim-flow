import flowtils as u

extensions = ["c"]

def run(**kw):
    command = "gcc %s; ./a.out" % kw.get("filepath")
    u.shell(command, **kw)


