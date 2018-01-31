## Hangman Project
## Computer Progamming II - Gavin Weiss

## Libraries
import time
import random

## Functions
def sleep():

    time.sleep(0.1)
    print("\n")
    return


## Code
sleep()
print("\t - Welcome to Hangman - ")

time.sleep(0.5)

sleep()
print("<-> A random word will be generated ")

sleep()
print("<-> You will have 5 guesses ")

sleep()
print("<-> Good Luck! ")

time.sleep(0.5)

sleep()

# Randomly Generated Word using list
words = ["python", "perl", "html", "ruby", "java"] # Word List
word = random.choice(words) # Randomizer

lives = 5 # Number of attempts

word_position = (0, len(word) - 1)

sleep()
print("> Guess a letter")

sleep()
guess1 = input("=> ")

if guess1 in word:

    sleep()
    print("Correct Guess")

else:

    sleep()
    print("Incorrect Guess")

    lives -= 1

    sleep()
    print("Lives = " + str(lives))

sleep()
print("> Guess a letter")

sleep()
guess2 = input("=> ")

if guess2 in word:

    sleep()
    print("Correct")

else:

    sleep()
    print("Incorrect Guess")

    lives -= 1

    sleep()
    print("Lives = " + str(lives))

sleep()
print("> Guess a letter")

sleep()
guess3 = input("=> ")

if guess3 in word:

    sleep()
    print("Correct Guess")

else:

    sleep()
    print("Incorrect Guess")

    lives -= 1

    sleep()
    print("Lives = " + str(lives))

if lives == 0:

    quit()
