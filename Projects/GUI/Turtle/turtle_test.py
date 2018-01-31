##########################################################################
## Unit 4 Lesson 3 - Turtle
## Computer Programming II - Gavin Weiss
##########################################################################


## Libraries
import time  # For timing
import random  # For randomization
import os # For running commands
import turtle # For a GUI 
from turtle import *
import tkinter # Needed by turtle
import turtle_functions # Seperate Functions File
from turtle_functions import * # Simpler function calling


#########################################################################
## Code
#########################################################################

loop = ("")

while loop == (""):

	question()
	turtle.resetscreen()

	# This will repeat the question function until 0 is selected

#########################################################################
screen.exitonclick() # This makes it so that clicking on the window exits
screen.mainloop() # This is so that turtle will loop itself
#########################################################################

