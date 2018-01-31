## Unit 3 Lesson 2 - While Loops
## Computer Programming II - Gavin Weiss

## Libraries
import time

## Code

# A while loop is similar to a for loop in that it runs through a block of code,
# a certain number of times

# The difference between the for loop and the while loop is that the for loop,
# has a fixed number of iterations (number of times), whereas the while runs
# until a certain condition is met

# Initialize a variable
# You can initialize a variable to anything, but it's common to use
# double quotes (""), or 0

pin = ("")

while pin != "12345":  # In honor of Spaceballs

    pin = input("\n\tPlease enter your 5 digit pin... ")

    if pin != "12345":

        print("\n\tYou have entered the wrong pin number.")

    print("\n\tACCESS GRANTED")

# pin, in this example is called a "sentry variable", or a loop variable
# It is the variable that is being checked against another value
# If you do not initialize the sentry variable, you will get an error
# Typically, it is initialized right before
