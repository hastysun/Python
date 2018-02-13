## Gavin Weiss - Computer Programming II
## Project - Poor Mans Paint


# A drawing object, that draws when dragged
# Must be able to turn drawing on and off
# Need to have a minimum of 4 pen sizes
# You must be able to clear your drawing
# Extra Credit : Show the current pen size


## Libraries
import time
import random
import turtle
import tkinter
from turtle import *


#> Turtle
dTurtle = turtle
screen = turtle.Screen()
screen.setup(800,600)
screen.Screen()
screen.title("Linux Paint")
dTurtle.showturtle()
screen.bgcolor("gray")
dTurtle.speed(0)
dTurtle.shapesize(2,2,2)

## Notes

# I realized that turtle can also be used
# as a screen, which solved my problem
# of there being two turtles.


#> Functions
def ClearScreen():

	dTurtle.clear()
	return

def On():

	dTurtle.penup()
	return

def Off():

	dTurtle.pendown()
	return

def PenSize1():

	dTurtle.pensize("1")
	return

def PenSize2():

	dTurtle.pensize("2")
	return

def PenSize3():

	dTurtle.pensize("3")
	return

def PenSize4():

	dTurtle.pensize("4")
	return

def PenSize10():

	dTurtle.pensize("10")

def ColorChanger():

	ColorList = ["lightgreen", "grey", "green", "blue", "red", "pink", "black"]
	RandomColor = random.choice(ColorList)
	dTurtle.color(RandomColor)
	return


#> Keybindings
onkey(ClearScreen, "r")
onkey(On, "o")
onkey(Off, "i")
onkey(ColorChanger, "c")
onkey(PenSize1, "1")
onkey(PenSize2, "2")
onkey(PenSize3, "3")
onkey(PenSize4, "4")
onkey(PenSize10, "5")


##> Main
dTurtle.ondrag(goto)


##> EOF
dTurtle.listen()
mainloop()
