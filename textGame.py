import random
import os

#This is the class information of the main, player character.
class MainCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gold = 0
        self.xp = 0
        self.hp = 10
        self.level = 1
        self.attack = random.randint(2,3)
        self.deathCount = 0
        self.killCount = 0
    def trainAttack(self, increaseAmt):
        self.attack = self.attack + increaseAmt
    def heal(self, increaseAmt):
        self.hp = self.hp + increaseAmt

class EasyBadGuy():
    def __init__(self, xp = 5):
        #Random naming comvention
        BadguyNames = ["Goblin", "Skeleton", "Bull", "Spider", "Ghost", "Gnoll", "Zombie", "Lion"]
        namePick = random.randint(0,7)

        self.name = BadguyNames[namePick]
        self.hp = random.randint(3,9)
        self.xp = xp
        self.attack = random.randint(1,3)
        self.luck = 1
        self.gold = random.randint(0,3)
        self.level = random.randint(0,2)
    def addAtk(self, increaseAmt):
        self.attack = self.attack + increaseAmt

class MedBadGuy():
    def __init__(self, xp = 12):
        self.name = "Troll"
        self.hp = random.randint(10,22)
        self.xp = xp
        self.attack = random.randint(7,16)
        self.luck = 2
        self.gold = random.randint(5,9)
    def addAtk(self, increaseAmt):
        self.attack = self.attack + increaseAmt

class HardBadGuy():
    def __init__(self, xp = 20):
        self.name = "Ogre"
        self.hp = random.randint(23,35)
        self.xp = xp
        self.attack = random.randint(20,40)
        self.luck = 3
        self.gold = random.randint(10,20)
    def addAtk(self, increaseAmt):
        self.attack = self.attack + increaseAmt

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
    os.system("CLS")

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
    userChoice = 0
    #the loop of the program. everything comes back to here unless they press 4 to exit
    while (userChoice != '4'):
        os.system("CLS")

        #checks to see if the player has enough health
        if (p1.hp <= 0):
            death(p1)
        #sees whether the player wants to fight, shop, train, or exit
        userChoice = townInfo()

        if (userChoice == '1'): #fight choice
            fightScreen(p1)
        elif (userChoice == '2'): #shop choice
            #the shop is where the player can buy stat upgrade trough weapons and armor
            print("shop place holder")
            adv()
        elif (userChoice == '3'): #learn spells choice
            #the libray is where the player learns new attacks and sees their stats
            trainScreen(p1)
    exit

#The screen to call up when you encounter a monster
def fightScreen(p1):
    while(True):
        os.system("CLS")

        #populates and enemy for the fight.
        enemy = enemyEncounter(p1)
        os.system("CLS")

        print(p1.name + " stumbled apon a level " + str(enemy.level) +" "+ enemy.name + "!\n")
        printInfo(enemy)
        adv()

        #checks to see if the current enemy is dead or not
        while (enemy.hp > 0):
            os.system("CLS")

            printInfo(enemy)
            print()
            printInfo(p1)
            print()
            #prints the enemy infor ^^ then asks the player what to do
            playerOption = input("- What would you like to do? -\n"+
                             "1. Fight\n"+
                             "2. Run\n>>")
            # attacks the enemy
            if (playerOption == '1'):
                os.system("CLS")
                attack(p1, enemy)
                #enemy only attacks back if their lucky enough
                if (enemy.hp > 0):
                    print("The " + enemy.name + " attacks!")
                    #tests the enemies luck against 1-3 (1 being lowest, 3 being never misses)
                    if (enemy.luck >= random.randint(1,3)):
                        attack(enemy, p1)

                        #checks to see if the player is dead or not
                        if (p1.hp <= 0):
                            death(p1)
                            return
                        else:
                            adv()
                    else:
                        print("But misses!")
                        adv()
            elif (playerOption == '2'):
                os.system("CLS")
                #WIP WIP WIP
                #if you run away you get no exp. will be a random chance though
                print("You coward!")
                enemy.hp = 0
                adv()
                return

        adv()
        #prints out the player xp amount if the enemy is beaten
        os.system("CLS")
        gainXp(p1, enemy)
        adv()

#a place where the player can train stats and heal using exp that they have earned.
#will add abilites
def trainScreen(p1):
    while(True):
        os.system("CLS")
        printInfo(p1)

        playerChoice = input("1. Train Attack\n" +
                             "2. Heal\n" +
                             "3. Exit\n>>")

        if (playerChoice == '1'):
            if(p1.xp >= 5):
                p1.xp = p1.xp - 5
                p1.trainAttack(1)
            else:
                print("Not enough experience points.\n Go fight more mobs!")
                adv()

        elif (playerChoice == '2'):
            if(p1.xp >= 3):
                p1.xp = p1.xp - 3
                p1.heal(2)
            else:
                print("Not enough experience points.\n Go fight more mobs!")
                adv()

        elif (playerChoice == '3'):
            return

#when the player dies during their adventure they come here to print out stats and start over
def death(p1):
    os.system("CLS")

    print("you ded")
    print("You earned " + str(p1.xp) + " exp!")
    p1.deathCount = p1.deathCount + 1
    print("You have died " + str(p1.deathCount) + " times on your journey so far!")
    p1.hp = 10
    adv()

#choses what enemy the player faces based on how many kills.
#this needs more complexity
def enemyEncounter(p1):
    if (p1.killCount <= 5):
        enemy = EasyBadGuy()

        #calculates a damage multiplier
        atkMultiplyer = random.randint(1,6)
        enemy.addAtk(atkMultiplyer)


    elif (p1.killCount <= 20):
        enemy = MedBadGuy()

        #calculates a damage multiplier
        atkMultiplyer = random.randint(7,16)
        enemy.addAtk(atkMultiplyer)

    elif (p1.killCount <= 40 or p1.killCount > 40):
        enemy = HardBadGuy()

        #calculates a damage multiplier
        atkMultiplyer = random.randint(20,30)
        enemy.addAtk(atkMultiplyer)
    return enemy

#Function for when someone atacks something
def attack(attacker, attackie):
    attack = attacker.attack
    print(attacker.name + " hit " + attackie.name + " for " + str(attack))
    attackie.hp = attackie.hp - attack
    print(attackie.name + "'s hp is now " + str(attackie.hp))
    print()

#anytime the player gains exp through battle it comes here
def gainXp(p1, enemy):
    print("You BEAT the " + enemy.name)
    print("You gained " + str(enemy.xp) + " experience!")
    p1.xp = p1.xp + enemy.xp
    p1.killCount = p1.killCount + 1
    print("For a player total of " + str(p1.xp))

#prints out the town info and grabs the players choice
def townInfo():
    os.system("CLS")

    print("Welcome to Stabby Village!")
    print("What would you like to do?\n")
    print("1. Fight monsters and gain rewards!")
    print("2. Spend that sweet, sweet gold.")
    print("3. Train in the magical arts.")
    print("4. Exit the town.")

    userChoice = input(">>")

    return userChoice

#This is where the player is sent to to create their new character.
def characterCreation():
    playerName = input("What is your characters name?\n>>")
    playerAge = input("How old is your character?\n>>")

    return MainCharacter(playerName, playerAge)

#Shows whoevers profile info
def printInfo(character):
    print("- " + character.name + " LV. " + str(character.level) + " -\n" +
          "Health = " + str(character.hp) + "\n" +
          "Attack = " + str(character.attack) + "\n" +
          "XP = " + str(character.xp) + "\n")

#advances the screen
def adv():
    print()
    input("Press 'Enter' to continue.")

#Starts the program.
main()
