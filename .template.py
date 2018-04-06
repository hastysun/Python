## Unit 5 Lesson 5 - Timers
## Computer Programming II - Gavin Weiss
  

## Libraries
import time
import random
import simpleguitk as simplegui


##> Define Global Variables



##> Define Helper Functions



##> Define Classes



##> Define Event Handlers
def draw(canvas):

    canvas.draw_text(VARIABLE, [32,32], 12, "Gray", "Monospace")



##> Create Frame
frame = simplegui.create_frame("SimpleGUI", 200, 200)



##> Register Event Handlers
frame.set_draw_handler(draw)



##> Start Frame and Timers
frame.start()

