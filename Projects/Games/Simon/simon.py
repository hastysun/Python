## Number Sequence Game
## Computer Progamming II - Gavin Weiss

## Libraries
import time
import random

## Functions
def sleep():

    time.sleep(0.1)
    print("\n")
    return

## Objective
# Program builds a sequence of numbers and user has to remember them
# Program says to do something, user must do it within certain time
    # Example:
    # "Type 9", user types 9
    # "Type 95", user types 95
    # "Type 956", user types 956
    # And so on

## Code

# Current list of numbers : 1 6 9 2 4 8 3 5 7

sleep()
print("\n\t -= WELCOME TO SIMON =- ")

sleep()
print(" - I WILL GIVE YOU A LETTER - ")

sleep()
print(" - YOU MUST TYPE THE LETTER AND THE ONE BEFORE IT - ")

sleep()
print(" - DO NOT FORGET THE LAST LETTER - ")

sleep()
time.sleep(0.5)
print("\t TYPE FAST OR DIE...")

sleep()
print("\n - 1 -")

sleep()
answer1 = int(input("=> "))

if answer1 ==(1):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50) # Skips 50 lines so user can't see previous number

sleep()
print("\n - 6 -")

sleep()
answer2 = int(input("=> " ))

if answer2 ==(16):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 9 - ")

answer3 = int(input("=> "))

if answer3 ==(169):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 2 - ")

answer4 = int(input("=> "))

if answer4 ==(1692):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 4 - ")

answer5 = int(input("=> "))

if answer5 ==(16924):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 8 - ")

answer6 = int(input("=> "))

if answer6 ==(169248):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 3 - ")

answer7 = int(input("=> "))

if answer7 ==(1692483):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

print("\n" * 50)

sleep()
print("\n - 5 - ")

answer8 = int(input("=> "))

if answer8 ==(16924835):

    sleep()

else:

    sleep()
    print("ERROR!")
    quit()

sleep()
print("\n - 7 - ")

answer9 = int(input("=> "))

if answer9 ==(169248357):

    sleep()
    print("\n\t - PASS - ")

    sleep()
    quit()

else:

    sleep()
    print("ERROR!")
    quit()
