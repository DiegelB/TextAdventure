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
        self.fearLevel = 0
    def trainAttack(self, increaseAmt):
        self.attack = self.attack + increaseAmt
    def heal(self, increaseAmt):
        self.hp = self.hp + increaseAmt
    def increaseFear(self):
        self.fearLevel = self.fearLevel + 1
    def resetFear(self):
        self.fearLevel = 0
    def giveGold(self, increaseAmt):
        self.gold = self.gold + increaseAmt
    def giveXp(self, increaseAmt):
        self.xp = self.xp + increaseAmt

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

#generates an adventure for the player. tracks amout of mobs and possible paths the player can take
class WalkingPath():
    def __init__(self, name, amtOfPaths, maxMobs, endingMaxGold):
        self.name = name
        self.amtOfPaths = amtOfPaths
        self.playerWalkedPaths = 0
        self.amtOfMobs = random.randint(1, maxMobs)
        self.endingGold = random.randint(30, endingMaxGold)
    def walkPath(self):
        self.amtOfPaths = self.amtOfPaths - 1
    def mobEncounter(self):
        self.amtOfMobs = self.amtOfMobs - 1
    def giveGold(self, p1):
        p1.gold = p1.gold + self.endingGold


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
    while (userChoice != 'exit'):
        os.system("CLS")
        #sees whether the player wants to fight, shop, train, or exit
        userChoice = townInfo()

        if (userChoice == 'walk'): #main game play loop
            if(p1.hp <= 0):
                print("Your health is too low, please go heal.")
                adv()
            else:
                walkAround(p1)
        elif (userChoice == 'gold'): #shop choice
            #the shop is where the player can buy stat upgrade trough weapons and armor
            print("shop place holder")
            print("gold: " + str(p1.gold))
            adv()
        elif (userChoice == 'train'): #learn spells choice
            #the libray is where the player learns new attacks and sees their stats
            trainScreen(p1)

    exit

#The screen to call up when you encounter a monster
def fightScreen(p1):
    os.system("CLS")

    #populates and enemy for the fight.
    enemy = enemyEncounter(p1)

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
                         "'Fight'\n"+
                         "'Run'\n>>")
        playerOption.lower()
        # attacks the enemy
        if (playerOption == 'fight'):
            os.system("CLS")
            attack(p1, enemy)
            #enemy only attacks back if their lucky enough
            if (enemy.hp > 0):
                print("\nThe " + enemy.name + " attacks!")
                #tests the enemies luck against 1-3 (1 being lowest, 3 being never misses)
                if (enemy.luck >= random.randint(1,3)):
                    attack(enemy, p1)

                    #checks to see if the player is dead or not
                    if (p1.hp <= 0):
                        adv()
                        death(p1)
                        return
                    else:
                        adv()
                else:
                    print("But misses!")
                    adv()
        elif (playerOption == 'run'):
            os.system("CLS")
            #WIP WIP WIP
            #if you run away you get a fear level. if its too high you cant fight anymore.
            print("You coward!")
            p1.increaseFear()
            print("Fear level now: " + str(p1.fearLevel))
            adv()
            break

    if(enemy.hp <= 0):
        adv()
        #prints out the player xp amount if the enemy is beaten
        os.system("CLS")
        gainXp(p1, enemy)
        adv()
    else:
        return

#a place where the player can train stats and heal using exp that they have earned.
#will add abilites
def trainScreen(p1):
    while(True):
        os.system("CLS")
        printInfo(p1)

        playerChoice = input("'Train' Attack\n" +
                             "'Heal'\n" +
                             "'Revive'\n" +
                             "'Exit'\n>>")
        playerChoice.lower()

        #Checks to se if the player has enough xp to level attack
        if (playerChoice == 'train'):
            if(p1.xp >= 5):
                p1.xp = p1.xp - 5
                p1.trainAttack(1)
            else:
                print("Not enough experience points.\n Go fight more mobs!")
                adv()

        #Checks to see if the player has exp to heal themselves,
        elif (playerChoice == 'heal'):
            if(p1.xp >= 3):
                p1.xp = p1.xp - 3
                p1.heal(2)
            else:
                print("Not enough experience points.\n Go fight more mobs!")
                adv()
        elif (playerChoice == 'revive'):
            if(p1.hp <= 0):
                p1.heal(10)
            else:
                print("Only for dead players!")
                adv()

        elif (playerChoice == 'exit'):
            return

#this is the main game play loop. You get a pre-generated place to walk through
#it has random mob encounters as well as extra goodie and loot to earn.
def walkAround(p1):
    #generates the (name, amount of path before win, max amount of mobs before win, max amount of gold youll earn)
    playerPathway = WalkingPath("Woodland Coast", 6, 10, 100)

    #checks to see if the pathway is completed or not
    while(playerPathway.amtOfPaths > 0):
        if(p1.hp <= 0): #if player is dead they cant continue
            return
        else:
            if(p1.fearLevel <= 2): #if player ran away too many times they cant continue or win
                os.system("CLS")
                print("Welcome to " + playerPathway.name + " " + p1.name + "\n")
                printInfo(p1)

                print(p1.name + "'s" + " fear level: " + str(p1.fearLevel))
                playerChoice = input("'Walk' forward or 'return' to town?\n>>")
                playerChoice.lower()

                if(playerChoice == 'walk'):
                    playerPathway.walkPath() #decreases 1 every time you walk throughh
                    if(playerPathway.amtOfMobs > 0):
                        if(random.randint(1,4) == 3): #75% chance youll get a mob encounter
                            print("\nYou advanced safely forward.\n")
                            adv()
                        else:
                            playerPathway.mobEncounter() #descreases 1 eveytime you fight a mob
                            fightScreen(p1)
                    else:
                        #if you beat all the mobs before advancing throuhh the are you get a bonus
                        print("\nYou've killed all the mobs in this area!")
                        print("Here is some extra goodies")
                        print("+100 gold, +100 xp")
                        p1.giveGold(100)
                        p1.giveXp(100)
                        playerPathway.amtOfPaths = 0
                        adv()
                elif(playerChoice == 'return'):
                    p1.resetFear()
                    return
            else:
                print("You've ran away too many times!")
                adv()
                p1.resetFear()
                return

    #if you beat all mobs or advance through the entire area (amtOfPaths) then you get loot!
    print("\nYou've left "+ playerPathway.name + ".")
    print(p1.name + " earned " + str(playerPathway.endingGold) + " gold.")
    playerPathway.giveGold(p1)
    adv()





#when the player dies during their adventure they come here to print out stats and start over
def death(p1):
    os.system("CLS")

    print("you ded")
    print("You earned " + str(p1.xp) + " exp!")
    p1.deathCount = p1.deathCount + 1
    print("You have died " + str(p1.deathCount) + " times on your journey so far!")
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
    print("'Walk' around to find monsters and loot!")
    print("Spend that sweet, sweet 'gold'.")
    print("'Train' in the magical arts.")
    print("'Exit' the town.")

    userChoice = input(">>")

    userChoice.lower()
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
          "XP = " + str(character.xp) + "\n" +
          "Gold = " + str(character.gold) + "\n")

#advances the screen
def adv():
    print()
    input("Press 'Enter' to continue.")

#Starts the program.
main()
