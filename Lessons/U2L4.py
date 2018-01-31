## Unit 2 Lesson 4 - Basic Functions
## Computer Programming II - Gavin Weiss

# These notes describe how to set up a basic function

# A function is a section of code that performs a defined task
# To use a defined function, we must "call" it
# A function should not be too big, and it should do one task
# Many functions are just a couple lines of code

## Libraries
import time  # For timing
import random  # For randomization

## Code

def greeting():

    # Must define function, called the "header"
    # The above statement is called a docstring
    # Not necessary to have a docstring, but good practice

    time.sleep(0.5)
    print("\n\tGood Morning, Nerd. How are you?")
    return

greeting()  # This calls the greeting function


def die_roll():

    roll = random.randint(1, 6)  # Is an integer

    time.sleep(0.5)
    print("\n\tYou rolled a " + str(roll))  # Must convert to string

    time.sleep(0.5)
    print("\n\t")
    return


die_roll()

# Homework - Due Monday, October 10th
# Call 5 original functions and call them
# 2 of them must have parameters
# Worth 10 points
