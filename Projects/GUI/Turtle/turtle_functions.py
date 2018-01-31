## Unit 4 Lesson 3 - Turtle
## Computer Programming II - Gavin Weiss

## Functions File 

## Libraries
import time  # For timing
import random  # For randomization
import os # For running commands
import turtle # For a GUI
import tkinter # Needed for turtle

##
screen = turtle.Screen() # This initializes the screen

sonic = turtle.Turtle() # This initializes the turtle

sonic.shape("arrow") # This defines the shape of the turtle

sonic.shapesize(1,2,1) # This defines the size of the turtle

screen.bgcolor("lightgreen") # This defines the background color

sonic.color("black") # This changes the color of the turtle

screen.screensize(256,256) # This sets the screen size

## Functions
def sleep():

    time.sleep(0.1)
    print("\n")

    return

def question():

	sleep()
	print("What shape would you like to view?")

	sleep()
	print("0 - Quit ")

	sleep()
	print("1 - Triangle ")

	sleep()
	print("2 - Square ")

	sleep()
	print("3 - Heptagon ")
	
	sleep()
	print("4 - Octagon ")

	sleep()
	print("5 - Decagon ")
	sleep()
	
	answer = input("> ")

	if answer == ("0"):

		sleep()
		quit()

	if answer == ("1"):

		sleep()
		triangle()
		sleep()

	if answer == ("2"):

		sleep()
		square()
		sleep()

	if answer == ("3"):
		
		sleep()
		heptagon()
		sleep()

	if answer == ("4"):

		sleep()
		octagon()
		sleep()

	if answer == ("5"):

		sleep()
		decagon()
		sleep()

	return

def triangle():

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(120)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(120)

	time.sleep(0.05)
	sonic.forward(100)

	return

def square():

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(90)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(90)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(90)

	time.sleep(0.05)
	sonic.forward(100)
		
	return


def heptagon():

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(50)

	return

def octagon():

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(60)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(40)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(50)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(60)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(40)

	time.sleep(0.05)
	sonic.forward(100)

	return


def decagon():

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)

	time.sleep(0.05)
	sonic.left(30)

	time.sleep(0.05)
	sonic.forward(100)
