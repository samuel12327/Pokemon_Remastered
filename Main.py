from Pokemon import Pokemon
from Pokemon import Opponent
from Grass import Grass
import time
import random

poke = Pokemon("CHARIZARD", "FIRE", "MALE", 100, 36, "x", "y")
opp = Opponent("ONYX", "ROCK", "FEMALE", 100, 35)
poke_moves = {"TACKLE": random.randrange(10, 30), "SCRATCH": random.randrange(5, 35), "BITE": random.randrange(0, 40)}
opp_moves = {"TACKLE": random.randrange(10, 30), "SCRATCH": random.randrange(5, 35), "BITE": random.randrange(0, 40)}
poke.setDefaultPosition()

def main():
    print("========================\n"
          "      POKEMON V1.1      \n"
          "========================\n")
    while True:
        action = input("WHAT DO YOU WANT TO DO?\n\n"
                       "[1] SHOW POKEMON\n"
                       "[2] WALK\n"
                       "[3] RESET LOCATION\n"
                       "[4] RESTORE HEALTH\n"
                       "[5] BATTLE\n"
                       "[6] QUIT GAME\n").upper()
        if action == "1":
            poke.showPokemon()
            time.sleep(1.5)
        elif action == "3":
            poke.setDefaultPosition()
            print("LOCATION IS RESET")
            time.sleep(1.5)
        elif action == "2":
            type = ["GRASS", "SAND", "WATER", "CAVE", "MOUNTAIN"]
            color = ["LIGHT", "DARK"]
            speed = [1, 2, 3, 2, 1]
            choiceofspeed = random.choice(speed)
            env = Grass(random.choice(color), random.choice(type), choiceofspeed)
            for i in env.showGrass():
                print(i)
            direction = input("INPUT DIRECTION (N/S/E/W): ").upper()
            distance = int(input("INPUT DISTANCE: "))
            time.sleep(choiceofspeed)
            poke.walk(direction, distance)
        elif action == "4":
            print("RESTORING HEALTH...")
            time.sleep(3)
            poke.setHP(100)
            print("HEALTH RESTORED!")
            print(poke.showName(), "is at 100 HP")
            print("")
            time.sleep(1)
        elif action == "5":
            print("========================\n"
                  "      YOUR OPPONENT     \n"
                  "========================\n")
            time.sleep(0.75)
            opp.showPokemon()
            time.sleep(1.5)
            print("")

            while True:
                choice = input("PICK MOVES:""\n""SCRATCH""\n""TACKLE""\n""BITE""\n""RUN").upper()
                if choice == "RUN":
                    chance = random.randrange(0, 2)
                    if chance == 1:
                        print("YOU HAVE ESCAPED SUCESSFULLY!")
                        time.sleep(0.5)
                        break
                    if chance == 0:
                        print("YOU FAILED TO ESCAPE!")
                        time.sleep(0.5)
                        enemy_attack = random.choice(list(opp_moves))
                        enemy_pick = opp_moves.get(enemy_attack)
                        poke.attack(enemy_pick)
                        print("Your Enemy used", enemy_attack)
                        time.sleep(0.5)
                        print("Damage was", enemy_pick)
                        time.sleep(0.5)
                        print("Your HP is: ")
                        print(poke.showHP())
                        time.sleep(0.5)


                else:
                    poke_pick = poke_moves.get(choice)
                    enemy_attack = random.choice(list(opp_moves))
                    enemy_pick = opp_moves.get(enemy_attack)
                    opp.attack(poke_pick)
                    poke.attack(enemy_pick)
                    print("You Used", choice)
                    time.sleep(0.5)
                    print("Damage was", poke_pick)
                    time.sleep(0.5)
                    print("Your Enemy's HP is: ")
                    print(opp.showHP())
                    time.sleep(1)
                    print("Your Enemy used", enemy_attack)
                    time.sleep(0.5)
                    print("Damage was", enemy_pick)
                    time.sleep(0.5)
                    print("Your HP is: ")
                    print(poke.showHP())
                    time.sleep(0.5)

                    if (opp.showHP()) < 0:
                        print("CHARIZARD WON!")
                        print("")
                        time.sleep(2)
                        break
                    if (poke.showHP()) < 0:
                        print("CHARIZARD FAINTED!")
                        print("")
                        time.sleep(2)
                        break
        if action == "6":
            print("SAVING GAME...")
            time.sleep(1.5)
            print("========================\n"
                  "        GAMEFREAK       \n"
                  "========================\n")
            time.sleep(1.5)
            break
main()
