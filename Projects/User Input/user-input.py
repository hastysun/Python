## Unit 5 Homework - User Input
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


## Code

# Define Global Veriables
length = 0
width = 0



# Define Helper Functions
def area():

	global length, width
	area = length * width
	result = (
			"The area of the rectangle is " + str(area) + " square units. "
			 )
	return result



# Define Classes

	# No classes needed



# Define Event Handlers
def RectLength(text):

	global length
	length = float(text)

def RectWidth(text):

	global width
	width = float(text)

def draw(canvas):

	canvas.draw_text(area(), [125, 200], 20, "green")
	# "canvas.draw" needs a string in the first position
	# This holds true for the function area() because
	# it's outputting a string



# Create a Frame
frame = simplegui.create_frame("Area Calculator", 600, 400)
frame.set_canvas_background("Grey")



# Register Event Handlers
frame.add_input("Length", RectLength, 100)
frame.add_input("Width", RectWidth, 100)
frame.set_draw_handler(draw)



# Start Frame and Timers
frame.start()
