## Unit 5 Lesson 4 - Button Canvas Interaction
## Computer Programming II - Gavin Weiss


# This program displays the letter being pressed
# on the canvas.


## Libraries
import time
import random
import simpleguitk as simplegui



## Define Global Variables
message = ("Long Live Pierce")
MessageOn = 0



## Define Helper Functions



## Define Classes



## Define Event Handlers
def draw(canvas):

	global message
	global MessageOn
	
	if MessageOn == 1:
		canvas.draw_text(message, [36, 64], 9, "gray")

def ReleaseMessage():

	global MessageOn

	MessageOn = 1


##> Create Frame
frame = simplegui.create_frame("SimpleGUI", 164, 64)



##> Register Event Handlers
PrintButton = frame.add_button("Print Message", ReleaseMessage)
frame.set_draw_handler(draw)



##> Start Frame and Timers
frame.start()
