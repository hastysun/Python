## Gavin Weiss - Janurary 2018
## Turtle Game


## Functions
import time
import random
import turtle
import tkinter
from turtle import *

## Turtle Initilization
screen = turtle.Screen()
arrow = turtle.Turtle()
arrow.shape("arrow")
arrow.shapesize(1,2,1)
arrow.speed(3)
arrow.color("grey")
screen.bgcolor("black")
screen.screensize(50,50)


## Functions
def sleep():

	time.sleep(0.05)
	return

def left():

	arrow.left(60)
	return

def left_fine():

	arrow.left(30)
	return

def up():
	
	arrow.forward(50)
	return

def down():

	arrow.backward(50)
	return

def right():

	arrow.right(60)
	return

def right_fine():
	
	arrow.right(30)
	return

def color():

	random_color_list = ["red","blue","green","grey","white","orange","brown","lightgreen"]

	random_color = random.choice(random_color_list)

	arrow.color(random_color)

def shape():

	random_shape_list = ["arrow","turtle","square","triangle","circle","classic"]

	random_shape = random.choice(random_shape_list)

	arrow.shape(random_shape)

def clear_screen():

	screen.reset()
	return

def quit_game():

	arrow.done()
	return


## Code
onkey(left,"a")
onkey(left_fine,"A")
onkey(up,"w")
onkey(down,"s")
onkey(right,"d")
onkey(right_fine,"D")
onkey(quit_game,"q")
onkey(shape,"r")
onkey(clear_screen,"x")
onkey(color,"c")

listen()


## End of file requirements
screen.mainloop()
