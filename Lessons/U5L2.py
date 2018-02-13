## Unit 5 Lesson 2 - Event Driven Example; Key Press Echo
## Computer Programming II - Gavin Weiss


# This program displays the letter being pressed
# on the canvas.


## Libraries
import time
import random
import simpleguitk as simplegui


## Code


## Define Global Variables
letter = ("")



## Define Helper Functions



## Define Classes



## Define Event Handlers
def KeyDown(key): # Local variable

	global letter
	letter = chr(key)

	# "chr" is a builtin Python function
	# that returns the key pressed in ASCII


def KeyUp(key):

	global letter
	letter = ("")

def draw(canvas):

	canvas.draw_text(letter, [32,32], 16, "Gray")



#5#> Create Frame
frame = simplegui.create_frame("Key Press Echo", 64, 64)



#6#> Register Event Handlers
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)
frame.set_draw_handler(draw)



#7#> Start Frame and Timers
frame.start()
