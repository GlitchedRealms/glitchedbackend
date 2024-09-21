import docker
dockerClient = docker.DockerClient()

def getContainers():
    containersReturn = []
    containers = dockerClient.containers.list(all=True)
    for container in containers:
        if imageName in str(container.image):
            containersReturn.append(container)
    return containersReturn


def removeContainers():
    containers = getContainers()
    for container in containers:
        if imageName in str(container.image):
            print("################################################### Deleting old container {}".format(container.name))
            try:
                container.stop()
                container.remove()
            except Exception as e:
                print("################################################### Error deleting old container {}".format(container.name))
                print(e)


def runContainer(testType,dataframeN):
    images = dockerClient.images.list(all=True)
    if imageName in ' '.join(map(str, images)):
        print("################################################### Image exist, starting container..")
        dockerClient.containers.run(imageName+":latest", environment = {"TEST_TYPE":testType,"DATAFRAME_N":dataframeN,"CALC_N":calcN})
    else:
        print("################################################### Image doesn't exist, need to create it!")
        dockerClient.images.build(path = "./", tag = imageName)
        dockerClient.containers.run(imageName+":latest", environment = {"TEST_TYPE":testType,"DATAFRAME_N":dataframeN,"CALC_N":calcN})


while True:
    userInput = input("Please input LIST, CREATE, or DELETE")
    