## Unit 5 Homework - Farenheight to Celcius
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


# Define Global Variables
farenheight = 0
celcius = 0


# Define Helper Functions
def answer():

	global farenheight, celcius
	answer = farenheight - 32
	result = (
				"The converted temperature is " + str(answer) + " degrees Celcius. "
			 )
	return result


# Define Classes


# Define Event Handlers
def Farenheight(text):

	global farenheight
	farenheight = float(text)


def Celcius(text):

	global ceclius
	celcius = float(text)

def draw(canvas):

	canvas.draw_text(answer(), [10, 50], 9, "black")


# Create a Frame
frame = simplegui.create_frame("Temperature Converter", 350, 150)
frame.set_canvas_background("darkgrey")


# Register Event Handlers
frame.add_input("Farenheight", Farenheight, 100)
frame.set_draw_handler(draw)


# Start Frame and Timers
frame.start()
