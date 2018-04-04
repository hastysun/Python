## Unit 5 Project - Pong 
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
BallPosition = [CanvasWidth / 2, CanvasHeight / 2]
BallRadius = 15
BallVelocity = 10
StartBall = 0
PongLabel = "Welcome to Pong"


## Event Handlers
def BallStart():

	global StartBall

	StartBall = 1

	return


def BallReset():

	global StartBall
	global BallPosition

	BallPosition = [CanvasWidth / 2, CanvasHeight / 2]

	StartBall = 0

	return


def KeyDown(key):

	global BallPosition
	global BallVelocity

	if key == simplegui.KEY_MAP['down']:

		BallPosition[1] = BallPosition[1] + BallVelocity

	elif key == simplegui.KEY_MAP['up']:

		BallPosition[1] = BallPosition[1] - BallVelocity

	elif key == simplegui.KEY_MAP['right']:

		BallPosition[0] = BallPosition[0] + BallVelocity

	elif key == simplegui.KEY_MAP['left']:

		BallPosition[0] = BallPosition[0] - BallVelocity


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


	if BallPosition == [300, 300]:

		BallVelocity = [-2, -2]


	if BallPosition == [0, 0]:
		
		BallVelocity = [2, 2]


## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)

GameTitle = frame.add_label("Welcome to Pong")

Spacer = frame.add_label("")


## Registered Event Handlers
frame.add_button("Start", BallStart, 50)
frame.add_button("Reset", BallReset, 50)


# frame.add_button("+ Velocity", IncreaseVelocity, 50)
# frame.add_button("- Velocity", DecreaseVelocity, 50)

frame.set_keydown_handler(KeyDown)
frame.set_draw_handler(draw)


## Init
frame.start()
