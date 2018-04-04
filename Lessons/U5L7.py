## Unit 5 Lesson 7 - Collision
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


##  Global Variables
CanvasWidth = 500
CanvasHeight = 400
BallPosition = [CanvasWidth / 2, CanvasHeight / 2]
BallRadius = 20
BallVelocity = [-4, 3]
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
		
		canvas.draw_circle(BallPosition, BallRadius, 2, "White", "Grey")


		# Bouncing off the left wall
		if BallPosition[0] <= BallRadius:

			BallVelocity[0] = - BallVelocity[0]


		# Bouncing off the right wall 
		if BallPosition[0] >= CanvasWidth - BallRadius:

			BallVelocity[0] = - BallVelocity[0]


		# Bouncing off the top wall
		if BallPosition[1] <= BallRadius:

			BallVelocity[1] = - BallVelocity[1]


		# Bouncing off the bottom wall
		if BallPosition[1] >= CanvasHeight - BallRadius:

			BallVelocity[1] = - BallVelocity[1]



## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)


## Registered Event Handlers
frame.add_button("Start", BallStart, 50)
frame.set_draw_handler(draw)


## Init
frame.start()
