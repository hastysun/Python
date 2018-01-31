## Unit 4 Lesson 2 - Classes and Objects Continued
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random
import os

## Functions
def sleep():

    time.sleep(0.1)
    print("\n")

    return

## Code
# A constructor is a special method defined in the first line of a class
# When you first construct an object from a class, you need to call the methods
# But with a constructor, the methods are automatically called
# An example, initiating values in a class

class Hero(object):

    """Creates a hero for a game"""

    def __init__(self, name, health, stamina):

        self.name = name
        self.health = health
        self.stamina = stamina

    def hero_stats(self):

        sleep()
        print(self.name + "'s" " current stats are: ")

        print("Health = " + str(self.health))

        print("Stamina = " + str(self.stamina))

    # In the class created above, "__init__" is a built in python method
    # With it, an objects attributes automatically created or initialized

warrior = Hero("Shane", 100, 100)

warrior.hero_stats()

# Next character
wizard = Hero("Harry", 50, 75)

sleep()

wizard.hero_stats()
