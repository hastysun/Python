## Homework - Functions Homework
## Gavin Weiss - Computer Programming II

## What to do
    # Create 5 original functions
    # Call them
    # 2 of them must be parameters

## Libraries
import time # For timing
import random # For randomization
import datetime # For the date and time function

## Code

time.sleep(1)
print("\n\t <> First Function <> ")

# First Function
def function1():

    time.sleep(0.1)
    print("\n")

    time.sleep(0.1)
    print("\n")

    time.sleep(0.5)
    print("\n\tThis is the first function!")

    time.sleep(0.1)
    print("\n")

    time.sleep(0.1)
    print("\n")

function1()

time.sleep(1)
print("\n\t <> Second Function <> ")

# Second Function
def function2():

    time.sleep(0.5)
    print("\n\tThe second function prints a random number.")

    random_number = random.randint(1, 100) # Is an integer

    time.sleep(1)
    print("\n\tYour random number is " + str(random_number)) # Must convert

    time.sleep(0.5)
    print("\n\t")
    return


function2()

time.sleep(1)
print("\n\t <> Third Function <> ")

# Third Function
def function3():

    time.sleep(0.5)
    print("\n\tThe third function prints the day of the month.")

    currentDT = datetime.datetime.now()

    time.sleep(0.5)
    print ("\n\tCurrent Day is of the month : %d" % currentDT.day)

    time.sleep(0.5)
    print("\n\t")

function3()

time.sleep(1)
print("\n\t <> Fourth Function <> ")

# Fourth Function
def function4():

    time.sleep(0.5)
    print("\n\tThe fourth function prints the current year.")

    currentDT = datetime.datetime.now()

    time.sleep(0.5)
    print ("\n\tCurrent Year is: %d" % currentDT.year)

    time.sleep(0.5)
    print("\n\t")

function4()

time.sleep(1)
print("\n\t <> Fifth Function <> ")

# Fifth Function
def function5():

    time.sleep(0.5)
    print("\n\tThe fifth function will tell you if the earth is flat.")

    time.sleep(0.5)
    print("\nAnd the answer is...")

    time.sleep(0.1)
    print("\n...")


    time.sleep(0.1)
    print("\n...")


    time.sleep(0.1)
    print("\n...")


    time.sleep(0.1)
    print("\n...")


    time.sleep(0.5)
    print("\n...")

    time.sleep(1)

    time.sleep(1)
    print("\nNo.")

function5()
