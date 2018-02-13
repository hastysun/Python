## Unit 5 Lesson 1 - Event Driven Programming
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


# Event driven programming is a model
# of computer programming in which the
# the program runs based on events that
# occur such as key presses, mouse clicks
# or a timer. In event driven programs, you have
# event listeners, such as key presses
# that set off functions, called event
# handlers. Linking an event listener to
# an event handler is called registering
# or binding.

# For our event driven programming,
# we will use a seven step structure


## The Seven Step Structure

#	1 - Define Global Variables
#	2 - Define Helper Functions
#	3 - Define Classes
#	4 - Define Event Handlers
#	5 - Create a Frame
#	6 - Register Event Handlers
#	7 - Start Frame and Timers
# A basic event-driven program


# Define global variables
message = "Hello World"


# Define helper functions

    # No helper functions for this program


# Define classes

    # No classes


# Define event handlers
def print_message(canvas):
    global message
    canvas.draw_text(message, [50, 100], 20, "red", "monospace")


# Create frame
frame = simplegui.create_frame("Test Message", 600, 400)
        #("Title", canvas width, canvas height)


# Note that the entire window is the frame and the output
# screen is the canvas
# As with most GUI's, the origin is in the upper left corner
# The coordiantes[50, 100] will go 50 pixels right
# and 100 pixels down


# Register event handlers
frame.set_draw_handler(print_message)


# Start frame and timers
frame.start()
