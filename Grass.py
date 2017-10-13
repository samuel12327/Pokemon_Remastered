from Environment import Environment

class Grass(Environment):

    def __init__(self, color, type, speed):
        Environment.__init__(self, type, speed)
        self.color = color

    def setColor(self, value):
        self.color = value

    def showGrass(self):
        color = self.color
        return (Grass.envone(self), "CONDITION: ", color, "\n")

    def envone(self):
        for i in Environment.getEnvType(self):
            return i

