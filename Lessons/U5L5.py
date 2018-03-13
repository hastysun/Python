## Unit 5 Lesson 5 - Timers
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


##> Define Global Variables
time = 0



##> Define Helper Functions



##> Define Classes



##> Define Event Handlers
def draw(canvas):

	canvas.draw_text(str(time), [50,60], 12, "Gray", "Monospace")
	
	return


def TimeInc():

	global time
	time = time + 1


##> Create Frame
frame = simplegui.create_frame("SimpleGUI", 150, 100)
timer = simplegui.create_timer(10, TimeInc)
# The first paremeter is time in milliseconds
# The second parameter is the function to run each time


##> Register Event Handlers
frame.set_draw_handler(draw)



##> Start Frame and Timers
timer.start()
frame.start()
