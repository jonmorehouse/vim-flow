import flowtils as u

extensions = ["go"]

def run(**kwargs):

    command = "go run %s" % kwargs.get("filepath")
    u.shell(command)
    

