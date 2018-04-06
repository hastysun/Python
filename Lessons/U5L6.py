## Unit 5 Lesson 6 - Ball Velocity
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


## Velocity
# Velocity is the speed of an object in a certain direction
# When coding with the velocity of an object, 
# we must deal with it's X and Y coordinates seperately


##  Global Variables
CanvasWidth = 300
CanvasHeight = 300
BallPosition = [CanvasWidth / 2, CanvasHeight / 4]
BallRadius = 30
BallVelocity = [1, 4]
StartBall = 0


## Event Handlers
def BallStart():

	global StartBall

	StartBall = 1

	return


def draw(canvas):

	global BallPosition
	global BallVelocity
	global BallRadius
	global StartBall

	canvas.draw_circle(BallPosition, BallRadius, 3, "White", "Grey")

	if StartBall == 1:

		BallPosition[0] = BallPosition[0] + BallVelocity[0]
		BallPosition[1] = BallPosition[1] + BallVelocity[1]

		# The "[0]" represents the X coordinate
		# The "[1]" represents the Y coordinate
		
		canvas.draw_circle(BallPosition, BallRadius, 3, "White", "Grey")


## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)


## Registered Event Handlers
frame.add_button("Start", BallStart, 50)
frame.set_draw_handler(draw)


## Init
frame.start()
