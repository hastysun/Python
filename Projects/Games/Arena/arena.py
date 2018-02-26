############################################
##                 Arena                  ##
## Gavin Weiss - Computer Programming II  ##
############################################

###############
## Libraries ##
###############
import time # Time Function
import random # Randomization
import arena_functions # Calls Functions 
from arena_functions import *

##########
## Code ##
##########
class Player(object):

# This is the "template"
# Both Players start from it

	def __init__(self, name, health):
	
		self.name = name # Player's name
		self.health = health # Player's health


	def stats(self): # This prints the current stats for a player

		sleep()
		print("- " + self.name + "'s current stats are - ")

		print("> Name = " + str(self.name))
		print("> Health = " + str(self.health))


intro() # This rolls the intro

player1 = Player("Player 1", 100) # Stats for Player 1; name and health
player2 = Player("Player 2", 100) # Stats for Player 2; name and health

time.sleep(1)
sleep()

print("Here are the current stats at turn 0.")

player1.stats() # This prints the name and health of Player 1
time.sleep(0.5)
player2.stats() # This prints the name and health of Player 2

sleep()
time.sleep(0.5)
print("A die roll will be made to decide who goes first.")
sleep()

goesfirst = ["Player 1", "Player 2"]
goesfirst_choice = random.choice(goesfirst)

if goesfirst_choice == ("Player 1"):

	opposite_choice = ("Player 2")
	opposite_choice_1 = player2

if goesfirst_choice == ("Player 2"):

	opposite_choice = ("Player 1")
	opposite_choice_1 = player1

time.sleep(1)
sleep()

print("=> " + goesfirst_choice + " goes first!")

time.sleep(0.5)
sleep()

############
## Turn 1 ##
############

sleep()
print(goesfirst_choice + ", what attack would you like to perform on " + opposite_choice + "?")
sleep()

time.sleep(1)

sleep()
print("= 1 > Punch")

sleep()
print("= 2 > Kick")

sleep()
attack_choice_1 = input("=> ")

# Attack List for a kick
kick_random_list = ["10", "15", "20", "100"]

# Attack list 
punch_random_list = ["10", "15", "20", "100"]

if attack_choice_1 == ("1"):

	sleep()
	print("=> You punch " + opposite_choice + ".")

	random_attack_punch_1 = random.choice(punch_random_list)
	
	sleep()
	print("=> " + random_attack_punch_1 + " points is dealt to " + opposite_choice + "'s HP.")	

	sleep()
	opposite_choice_1.health = opposite_choice_1.health - int(random_attack_punch_1)
	
	time.sleep(1)

if attack_choice_1 == ("2"):

	sleep()
	print("=> You kick " + opposite_choice + ".")

	random_attack_kick_1 = random.choice(kick_random_list)

	sleep()
	print("=> " + random_attack_kick_1 + " points is dealt to " + opposite_choice + "'s HP.")

	sleep()
	opposite_choice_1.health = opposite_choice_1.health - int(random_attack_kick_1)

	time.sleep(1)

time.sleep(1)

sleep()
print(goesfirst_choice + " has finished their turn.")

if player1.health == 0:

	sleep()
	print("Player 2 wins!")
	quit()
	
if player2.health == 0:

	sleep()
	print("Player 1 wins!")
	quit()


sleep()
print("Here are the current stats after turn 1.")

sleep()
player1.stats()
player2.stats()

time.sleep(3)

lines()

############
## Turn 2 ##
############

if goesfirst_choice == ("Player 1"):

	turn_2_offense = ("Player 2")
	turn_2_offense_1 = player2

	turn_2_defense = ("Player 1")
	turn_2_defense_1 = player1	
	
if goesfirst_choice == ("Player 2"):

	turn_2_offense = ("Player 1")
	turn_2_offense_1 = player1
	
	turn_2_defense = ("Player 2")
	turn_2_defense_1 = player2

sleep()
print("It is now " + turn_2_offense + "'s turn.")

sleep()
print(turn_2_offense + ", what move would you like to make on " + turn_2_defense + "?")

sleep()
print("= 1 > Punch")

sleep()
print("= 2 > Kick")

sleep()
attack_choice_2 = input("=> ")

if attack_choice_2 == ("1"):

	sleep()
	print("=> You punch " + turn_2_defense + ".")
	
	random_attack_punch_2 = random.choice(punch_random_list)

	sleep()
	print("=> " + random_attack_punch_2 + " points is dealt to " + opposite_choice + "'s HP.")	

	sleep()
	turn_2_defense_1.health = turn_2_defense_1.health - int(random_attack_punch_2)

if attack_choice_2 == ("2"):

	sleep()
	print("=> You kick " + turn_2_defense + ".")
	
	random_attack_kick_2 = random.choice(kick_random_list)

	sleep()
	print("=> " + random_attack_kick_2 + " points is dealt to " + opposite_choice + "'s HP.")

	sleep()
	turn_2_defense_1.health = turn_2_defense_1.health - int(random_attack_kick_2)


if player1.health == 0:

	sleep()
	print("Player 2 wins!")
	sleep()

	quit()
	
if player2.health == 0:

	sleep()
	print("Player 1 wins!")
	sleep()
	
	quit()

time.sleep(1)

sleep()
print("Here are the current stats after turn 2.")

sleep()
player1.stats()
player2.stats()

time.sleep(1)

############
## Turn 3 ##
############
