class Pokemon():
    def __init__(self, name, type, gender, hp, level, x, y):
        self.name = name
        self.type = type
        self.gender = gender
        self.hp = hp
        self.level = level
        self.positionx = x
        self.positiony = y
    def setDefaultPosition(self):
        self.positionx = 0
        self.positiony = 0
    def showPokemon (self):
        print("NAME:", self.name)
        print("TYPE:", self.type)
        print("GENDER:", self.gender)
        print("HP:", self.hp)
        print("LEVEL:", self.level)
        print("LOCATION:", "(",  self.positionx, ",", self.positiony, ")")
        print("\n")
    def showName (self):
        return self.name
    def walk(self, direction, distance):
        if direction == "N":
            self.positiony = int(self.positiony + distance)
            print("LOCATION:", "(",  self.positionx, ",", self.positiony, ")")
            print("\n")
        if direction == "S":
            self.positiony = self.positiony - distance
            print("LOCATION:", "(",  self.positionx, ",", self.positiony, ")")
            print("\n")
        if direction == "E":
            self.positionx = self.positionx + distance
            print("LOCATION:", "(",  self.positionx, ",", self.positiony, ")")
            print("\n")
        if direction == "W":
            self.positionx = self.positionx - distance
            print("LOCATION:", "(",  self.positionx, ",", self.positiony, ")")
            print("")
    def setHP(self, hp):
        self.hp = hp
    def showHP(self):
        return self.hp
    def attack(self, damage):
        self.hp = self.hp - damage

class Opponent:
    def __init__(self, name, type, gender, hp, level):
        self.name = name
        self.type = type
        self.gender = gender
        self.hp = hp
        self.level = level
    def showPokemon (self):
        print("NAME:", self.name)
        print("TYPE:", self.type)
        print("GENDER:", self.gender)
        print("HP:", self.hp)
        print("LEVEL:", self.level)
    def attack(self, damage):
        self.hp = self.hp - damage
    def showHP(self):
        return self.hp
