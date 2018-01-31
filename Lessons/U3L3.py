## Unit 3 Lesson 3 - Tuples
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random

## Code

# Tuples are sequences that contain elements of any type
# Tuples are lists that are "immutable", which means unchangeable
# Tuples can be strings, numbers, images, sound files, etc.
# You can't edit Tuples
# But you can create new ones by concatenating other Tuples

satchel = ()  # This is an empty tuple

# Like other values in Python, it can be treated as a condition
# An empty tuple is false
# A tuple with at least one element is true

if not satchel:  # if satchel != true

    time.sleep(0.5)
    print("\nYou currently have no items in your satchel.")

print("\n")
print(satchel)

print("\nAs you search your world, you start collecting useful items.")

satchel = ("Sword", "Shield", "Potion")

print(satchel)

# Tuples can be written across multiple lines

satchel = ("Sword",
           "Shield",
           "Potion")

print("\n")
print(satchel)


def inv():  # Function to see whats in the satchel

    time.sleep(0.5)
    print("\n")

    time.sleep(0.5)
    print(satchel)


inv()

# We can use the "len" function to see the number of items in our tuple

time.sleep(0.5)
print("\nYou have " + str(len(satchel)) + " items in your satchel.")

# You can check to see if an item is in a tuple

if "Sword" in satchel:

    time.sleep(0.5)
    print("\nYou have a sword to attack foes.")

if "Shield" in satchel:

    time.sleep(0.5)
    print("\nYou have a shield to defend yourself.")

if "Potion" in satchel:

    time.sleep(0.5)
    print("\nYou have a potion to heal yourself.")

else:

    time.sleep(0.5)
    print("\nYou do not have the basic needed items, please obtain them.")

# Concatenating Tuples

chest = ("10 gold pieces", "Power Ring")

time.sleep(0.5)
print("\nWhile wandering through the woods, you come across a chest.")

time.sleep(0.7)
print("\nThe chest contains: ")

for items in chest:

    time.sleep(0.5)
    print(items)

time.sleep(0.5)
print("\nBelieving these items to be useful, you place them into your satchel.")

satchel += chest

time.sleep(0.5)
print("\nHere are the current items in your inventory:")

inv()
