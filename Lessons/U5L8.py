## Unit 5 Lesson 8 - Moving an Object
## Computer Programming II - Gavin Weiss


## TODO 
# Make a square as the ball
# Get it to move


## Libraries
import time
import random
import simpleguitk as simplegui


##  Global Variables
CanvasWidth = 500
CanvasHeight = 500

BallPosition = [CanvasWidth / 2, CanvasHeight / 2]
BallRadius = 20
BallVelocity = [-4, 3]
StartBall = 0

SquarePointList = [(10, 20), (20, 30), (30, 10)]
SquareWidth = 10
SquareLineColor = "Grey"
StartSquare = 0

DrawVariables = [
                "BallPosition", "BallVelocity", "BallRadius", "StartBall", 
                "SquarePointList", "SquareWidth", "SquareLineColor", "StartSquare"
                ]


## Event Handlers
def BallStart():

        global StartBall

        StartBall = 1

        return


def SquareStart():

        global StartSquare

        StartSquare = 1

        return


def draw(canvas):

        global DrawVariables


      # canvas.draw_circle(BallPosition, BallRadius, 3, "White", "Grey")


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


        if StartSquare == 1:

                BallPosition[0] = BallPosition[0] + BallVelocity[0]
                BallPosition[1] = BallPosition[1] + BallVelocity[1]

                # The "[0]" represents the X coordinate
                # The "[1]" represents the Y coordinate
                
                canvas.draw_polygon(SquarePointList, SquareWidth, SquareLineColor)


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




        # Borders
        canvas.draw_polygon([(0, 0), (0, 500)], 10, "Grey")
        canvas.draw_polygon([(500, 0), (0, 0)], 10, "Grey")
        canvas.draw_polygon([(500, 500), (500, 0)], 5, "Grey")
        canvas.draw_polygon([(0, 500), (500, 500)], 5, "Grey")



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



## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)



## Registered Event Handlers
frame.add_button("Start", BallStart, 50)
frame.add_button("Start", StartSquare, 50)
frame.set_keydown_handler(KeyDown)
frame.set_draw_handler(draw)


## Init
frame.start()
