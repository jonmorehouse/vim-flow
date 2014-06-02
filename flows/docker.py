import flowtils as u

filenames = ["Dockerfile", "Dockerfile"]

#Propose the idea of putting a ".docker" file in the directory
#This could potentially be used as the run command?
#For now, building with the tag seems like a safe default

# shell into the docker box
def alt(**kw):

    command = "docker run -i -t %s --entrypoint=/bin/bash" % kw.get("directory_name")


# build docker file by default
def run(**kw):

    command = "cd %s && " % kw.get("basepath")
    command += "docker build -t %s ." % kw.get("directory_name")

    u.shell(command)
