class Environment:

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def setEnvType(self, type):
        self.type = type

    def setEnvSpeed(self, speed):
        self.speed = speed

    def getEnvType(self):
        return "ENVIRONMENT:\n" + str(self.type), "\n"
