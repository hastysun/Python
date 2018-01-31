## Project - Insultinator
## Computer Progamming II - Gavin Weiss, October 30th 2017

#! Due Thursday

## Libraries
import time
import random

## Code
# Focused on using lists
# 4 Lists, with 4 insults each

time.sleep(0.5)
print("\n\t - Ready to get insulted? - ")

time.sleep(0.1)
print("\n")

# Lists of insults
insult1 = ["dumb", "stupid", "weird", "lazy"]
insult2 = ["idiotic", "clumsy", "dull", "ugly" ]
insult3 = ["annoying", "unfunny", "boring", "disgraceful"]
insult4 = ["scratch-user", "scratch-user", "scratch-user", "scratch-user"]

# Randomizer
insult1a = random.choice(insult1)
insult2a = random.choice(insult2)
insult3a = random.choice(insult3)
insult4a = random.choice(insult4)

# Function for outcome of insult
def insult():

    print(
         (str("\nYou are a ")) + str((insult1a)) + str(", ") + str(insult2a) +
         str(", ") + str(insult3a) + str(", ") + str(insult4a) + str(".")
         )

    return

insult()

# Ending
time.sleep(1)
print("\n\tThank's for playing idiot!")

time.sleep(0.5)
print("\n")
