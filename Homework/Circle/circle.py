## Unit 5 Homework - Circle
## Computer Programming II - Gavin Weiss


# Prints a circle
# Two buttons to increase and decrease radius
# Prints the current radius
# Have a minumum and maximum


## Libraries
import time
import random
import simpleguitk as simplegui


##> Define Global Variables
CircleRadius = 30


##> Define Helper Functions


##> Define Classes


##> Define Event Handlers
def draw(canvas):

	global CircleRadius

	center = (100, 100)
	line_width = 1
	line_color = "grey"
	circle = canvas.draw_circle(center, CircleRadius, line_width, line_color)

	canvas.draw_text(CircleRadius, [92, 107], 9, "grey")	

	return circle


def IncreaseRadius():

	global draw
	global CircleRadius

	if CircleRadius > 90:

		print("Maximum")	

	if CircleRadius < 90:

		CircleRadius += 10

	draw()
	
	return CircleRadius
	return draw


def DecreaseRadius():

	global draw
	global CircleRadius

	if CircleRadius < 20:

		print("Minimum")
	
	if CircleRadius > 20:
	
		CircleRadius -= 10
	
	draw()

	return CircleRadius
	return draw


##> Create Frame
frame = simplegui.create_frame("SimpleGUI", 200, 200)


##> Register Event Handlers
frame.add_button("Increase", IncreaseRadius)
frame.add_button("Decrease", DecreaseRadius)
frame.set_draw_handler(draw)


##> Start Frame and Timers
frame.start()
