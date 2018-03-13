## Computer Programming II - Group Project : Number Guessing Game
## Gavin Weiss, Riley Nelson, and John

## Psuedo Code

## Libraries
import random
import time

## Code

#Initialize correct number variable, set it to random (1, 100)
#Initialize variable to track # of guesses, set it to [how many guesses should we allow guys?]
#Print basic instructions
while input is invalid (not a number between 1 and 100):
    	print("invalid input")
#Initialize guess variable, set it to user guess input
while number guessed is incorrect and guess# > 0:
	if guess is less than correct:
		Print “too low”
	if guess is higher than correct:
		Print “too high”
	set guess to user input
	set guess# -= 1
	print(("You have" + [guess]) + "tries left")
if guess# = 0 and guess is incorrect:
	print("Game Over")
if guess is correct:
	print("Correct")
