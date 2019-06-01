import random 
import os 

#This is the class information of the main, player character.
class MainCharacter():
    def __init__(self, name, age, xp=0):
        self.name = name
        self. age = age
        self.xp = xp
        self.hp = 100
        self.level = 1
        self.attack = random.randint(2,8)

class EasyBadGuy():
    def __init__(self, xp = 5):
        self.name = "Goblin"
        self.hp = random.randint(3,9)
        self.xp = xp
        self.attack = random.randint(1,2)
        self.luck = 1

#The main funtion. It starts the program then sets the players character
#whether its loaded in or created.
def main():
    loadFile = startScreen()
    #creates a new chatacter for the player
    if (loadFile == ''):
        classInfo = characterCreation()
        p1 = classInfo
        mainLoop(p1)
    #loads in the players existing chacter (WORK IN PROGRESS)
    else:
        p1 = MainCharacter(loadFile, 21)
        mainLoop(p1)

#This is the starting screen. it asks if the player has played then either 
#sends them to create a character, or loads there previous character in.
def startScreen():
    os.system("clear")

    print("Welcome to the amazing\n"+
          " TeXt BaSeD AdVeNtUrE\n")

    returnPlayer = input("- Have you played before? -\n"+
                         "If yes, please type your adventurer's name\n"+
                         "If no, please type 'no'\n>>")

    if (returnPlayer == 'no' or returnPlayer == 'No' or returnPlayer == ''):
        return ''
    else:
        return returnPlayer

#this is the main loop. generates bad guys, has a shop, picks abilites
def mainLoop(p1):
    os.system("clear")
    #populates an easy bad guy for the player
    easyBadGuy = EasyBadGuy() 
    print("Welcome " + p1.name + " you are looking mighty tough!\n" +
          "Fight this " + easyBadGuy.name + ", you " + str(p1.age) + " year old!!\n")
    adv()
    fightScreen(p1, easyBadGuy)

#The screen to call up when you encounter a monster
def fightScreen(p1, enemy):
    os.system("clear")
    #checks to see if the current enemy is dead or not
    while (enemy.hp > 0):
        os.system("clear")
        printInfo(enemy)
        print()
        print("Your HP: " + str(p1.hp) + "\n")
        #prints the enemy infor ^^ then asks the player what to do
        playerOption = input("- What would you like to do? -\n"+
                         "1. Fight\n"+
                         "2. Run\n>>")
        # attacks the enemy
        if (playerOption == '1'):
            os.system("clear")
            attack(p1, enemy)
            #enemy only attacks back if their lucky enough
            if (enemy.hp > 0):
                print("The " + enemy.name + " attacks!")
                #tests the enemies luck against 1-3 (1 being lowest, 3 being never misses)
                if (enemy.luck >= random.randint(1,3)):
                    attack(enemy, p1)
                    adv()
                else:
                    print("But misses!")
                    adv()
        else:
            print("")
    
    adv()
    #prints out the player xp amount if the enemy is beaten
    os.system("clear")
    gainXp(p1, enemy)
    

#Function for when someone atacks something
def attack(attacker, attackie):
    attack = attacker.attack
    print(attacker.name + " hit " + attackie.name + " for " + str(attack))
    attackie.hp = attackie.hp - attack
    print(attackie.name + "'s hp is now " + str(attackie.hp))
    print()

def gainXp(p1, enemy):
    print("You BEAT the " + enemy.name)
    print("You gained " + str(enemy.xp) + " experience!")
    p1.xp = p1.xp + enemy.xp
    print("For a player total of " + str(p1.xp))


#This is where the player is sent to to create their new character. 
def characterCreation():
    playerName = input("What is your characters name?\n>>")
    playerAge = input("How old is your character?\n>>")

    return MainCharacter(playerName, playerAge)

#Shows whoevers profile info
def printInfo(character):
    print("- " + character.name + " -\n" +
          "Health = " + str(character.hp) + "\n" +
          "Attack = " + str(character.attack) + "\n" +
          "XP = " + str(character.xp) + "\n") 
          

#advances the screen
def adv():
    print()
    input("Press 'Enter' to continue.")
    

#Starts the program.
main()