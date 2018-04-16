## Unit 5 Lesson 8 - Pong Game
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


## Global Variables
CanvasWidth = 400
CanvasHeight = 400

PaddlePosition = [10, 200]

PaddleHeight = 10
PaddleWidth = 4
PaddleColor = "Grey"

X_Velocity = 0
Y_Velocity = 0

        
## Main
def KeyDown(key):

    global CanvasHeight
    global CanvasWidth
    global PaddlePosition
    global X_Velocity
    global Y_Velocity

    
    Acceleration = 1

    if key == simplegui.KEY_MAP['down']:

       Y_Velocity = Y_Velocity - Acceleration

    elif key == simplegui.KEY_MAP['up']:

       Y_Velocity = Y_Velocity + Acceleration


    return Acceleration



def KeyUp(key):

    global CanvasHeight
    global CanvasWidth
    global PaddlePosition
    global X_Velocity
    global Y_Velocity
    global Acceleration

    
    Acceleration = 0

    if key == simplegui.KEY_MAP['down']:

            X_Velocity = X_Velocity - Acceleration

    elif key == simplegui.KEY_MAP['up']:

            X_Velocity = X_Velocity - Acceleration


    return



def draw(canvas):

    global CanvasWidth
    global CanvasHeight
    global PointA
    global PointB
    global PointC
    global PointD
    global PaddleHeight
    global PaddleWidth
    global PaddlePosition
    global X_Velocity
    global Y_Velocity
    global PaddleWidth
    global PaddleColor

    PaddlePosition[0] = PaddlePosition[0] + X_Velocity
    PaddlePosition[1] = PaddlePosition[1] - Y_Velocity
    
   # canvas.draw_polygon([PointA, PointB, PointC, PointD], PaddleWidth, "Grey")
    canvas.draw_polygon([
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 10], 
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 10], 
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 60],
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 60]],
                        PaddleWidth, PaddleColor)

    
    # Paddle Gutter
    canvas.draw_polygon([(40, 0), (40, 400)], 4, "Grey")


    # Borders
    canvas.draw_polygon([(0, 0), (0, 400)], 10, "Grey")
    canvas.draw_polygon([(400, 0), (0, 0)], 10, "Grey")
    canvas.draw_polygon([(400, 400), (400, 0)], 5, "Grey")
    canvas.draw_polygon([(0, 400), (400, 400)], 5, "Grey")



## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)


## Init
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)
frame.set_draw_handler(draw)
frame.start()
