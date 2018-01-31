## Unit 4 Lesson 3 - Turtle
## Computer Programming II - Gavin Weiss


## Libraries
import time  # For timing
import random  # For randomization
import os # For running commands
import turtle # For a GUI
import tkinter


## Functions
def sleep():

	time.sleep(0.1)
	print("\n")

	return


## Code

# Create (instantiate) an object named "sonic" from the turtle class"

# We can set the shape of the object
# Initial shapes are "arrow", "turtle", "circle", "square", etc.


# We can instantiate an object to be the background from the Screen() class

screen = turtle.Screen()

sonic = turtle.Turtle()

sonic.shape("arrow")

sonic.shapesize(3,3,3)

screen.bgcolor("lightgreen")

screen.exitonclick()

# Turtle can use CSS
# We can define functions to help control the movement of our object


def go_left():
	
	sonic.left(50) # Note that left and right deal with angle turns, not moving
	return

def go_right():

	sonic.right(5)
	return

def go_forward():
	
	sonic.forward(10) # Forward and backwards deal with distance moved
	return


# We can use the "onkey" method to bind keyboard keys to the movement of the object
#screen.onkey(go_left, "a")
#screen.onkey(go_right, "d")
#screen.onkey(go_forward, "w")
#screen.onkey(go_backward, "s")

sleep()
screen.mainloop()
