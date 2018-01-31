## Unit 4 Project - Two Player Game
## Gavin Weiss - Computer Programming II

## The Elder Scrolls X
# A fan made 2 player game successor the The Elder Scrolls Series
    # Two players start off in an arena
    # Can choose starting items
    # Can choose classes

## Libraries
import time # Self explanatory
import random # Self explanatory
import os # Used for Linux commands
import os, platform # For Linux intro

## Functions
def sleep(): # This function just automates what I usually do manually

    time.sleep(0.1)
    print("\n")

    return

## Code
class Player1(object): # This is the class for Player 1

    def __init__(self, name, health, attack, stamina, defense):

        self.name = name # Player's name
        self.health = health # Player's max health
        self.attack = attack # Player's attack power, can be changed
        self.stamina = stamina # How many attacks you can do
        self.defense = defense # How much damage you take

    def Stats(self):

        sleep()
        print(self.name + "'s currents stats are: ")

        sleep()
        print("Health = " + str(self.health))
        print("Attack = " + str(self.attack))
        print("Stamina = " + str(self.stamina))
        print("Defense = " + str(self.defense))
        sleep()

class Player2(object): # This is the class for Player 2

    def __init__(self, name, health, attack, stamina, defense):

        self.name = name
        self.health = health
        self.attack = attack
        self.stamina = stamina
        self.defense = defense

    def Stats(self):

        sleep()
        print(self.name + "'s currents stats are: ")

        sleep()
        print("Health = " + str(self.health))
        print("Attack = " + str(self.attack))
        print("Stamina = " + str(self.stamina))
        print("Defense = " + str(self.defense))
        sleep()

def intro1(): # This is an intro for Linux

    sleep()
    os.system("figlet Elder Scrolls X")
    sleep()

    return

def intro2(): # Intro for anything else

    sleep()
    print("\n\t Elder Scrolls X")
    sleep()

    return

if platform.system() == "Linux":

    intro1()

else:

    intro2()

def CharCreation(): # Function to ask questions for class choosing

    sleep()
    print("=> What kind of class do you want?")

    sleep()
    print("> 1 - Knight")

    #sleep()
    print("> 2 - Thief")

    #sleep()
    print("> 3 - Lancer")

    sleep()

    return

sleep()
print("=> Player 1 : What is your name?")

name1 = input("> ") # "name1" is Player 1's name

sleep()

print("=> Player 1,")

CharCreation()

CharCreationChoice1 = input("> ")

if CharCreationChoice1 == ("1"): # Knight

    player1 = Player1(name1, 200, 150, 50, 200)

if CharCreationChoice1 == ("2"): # Thief

    player1 = Player1(name1, 100, 200, 100, 50)

if CharCreationChoice1 == ("3"): # Lancer

    player1 = Player1(name1, 100, 100, 100, 100)

sleep()

player1.Stats() # Prints the stats for Player 1

sleep()
print("=> Player 2 : What is your name?")

name2 = input("> ") # "name2" is Player 2's name

CharCreation()

CharCreationChoice2 = input("> ")

if CharCreationChoice2 == ("1"): # Knight

    player2 = Player2(name2, 200, 150, 50, 200)

if CharCreationChoice2 == ("2"): # Thief

    player2 = Player2(name2, 100, 200, 100, 50)

if CharCreationChoice2 == ("3"): # Lancer

    player2 = Player2(name2, 100, 100, 100, 100)

player2.Stats() # Prints Player 2's stats
