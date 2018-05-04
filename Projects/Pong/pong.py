## Unit 5 Lesson 8 - Pong Game
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


## Global Variables

# Canvas
CanvasWidth = 400
CanvasHeight = 400
Score = 0

# Ball
BallPosition = [CanvasWidth / 2, CanvasHeight / 2]
BallRadius = 10
BallVelocity = [-1, 2]

# Paddle
PaddlePosition = [5, 200]
PaddleHeight = 10
PaddleWidth = 5
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

    if key == simplegui.KEY_MAP['j']:

       Y_Velocity = -2

    elif key == simplegui.KEY_MAP['k']:

       Y_Velocity = 2


    return Acceleration



def KeyUp(key):

    global CanvasHeight
    global CanvasWidth
    global PaddlePosition
    global X_Velocity
    global Y_Velocity
    global Acceleration

    
    Acceleration = 0

    if key == simplegui.KEY_MAP['j']:

        Y_Velocity = 0

    elif key == simplegui.KEY_MAP['k']:

        Y_Velocity = 0


    return



def draw(canvas):

    global CanvasWidth
    global CanvasHeight
    global PaddleHeight
    global PaddleWidth
    global PaddlePosition
    global X_Velocity
    global Y_Velocity
    global PaddleWidth
    global PaddleColor
    global BallPosition
    global BallVelocity
    global BallRadius
    global Score


    # Draw the ball
    canvas.draw_circle(BallPosition, BallRadius, 1, "Grey", "Black")



    # Bouncing off the paddle
    # This takes care of X coordinates 
    if BallPosition[0] - BallRadius <= PaddlePosition[0] + PaddleWidth / 2:

        if BallPosition[1] + BallRadius < PaddlePosition[1] + PaddleHeight / 2: 
                
            if BallPosition[0] + BallRadius > PaddlePosition[0] + PaddleHeight / 2:

                BallVelocity[0] = - BallVelocity[0] 
                Score = Score + 1
                ScoreLabel.set_text(Score)
                print("Score")




    # Left wall
    if BallPosition[0] == 0: 

        print("Game Over")
        Score = 0
        ScoreLabel.set_text("Game Over")


    # Bouncing off the right wall
    if BallPosition[0] >= CanvasWidth - BallRadius:

            BallVelocity[0] = - BallVelocity[0]


    # Bouncing off the top wall
    if BallPosition[1] <= BallRadius:

            BallVelocity[1] = - BallVelocity[1]


    # Bouncing off the bottom wall
    if BallPosition[1] >= CanvasHeight - BallRadius:

            BallVelocity[1] = - BallVelocity[1]



    # Ball
    BallPosition[0] = BallPosition[0] + BallVelocity[0]
    BallPosition[1] = BallPosition[1] + BallVelocity[1]

    # Paddle
    PaddlePosition[0] = PaddlePosition[0] + X_Velocity
    PaddlePosition[1] = PaddlePosition[1] - Y_Velocity

    
    # Draw the paddle
    canvas.draw_polygon([
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 10], 
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 10], 
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 50],
                        [PaddlePosition[0] + 10, PaddlePosition[1] - 50]],
                        PaddleWidth, PaddleColor)

    if PaddlePosition[1] == 60:

        Y_Velocity = 0

    
    if PaddlePosition[1] == 410:
    
        Y_Velocity = 0

    
    # Paddle Gutter


    # Borders
    canvas.draw_polygon([(0, 0), (0, 400)], 10, "Grey")
    canvas.draw_polygon([(400, 0), (0, 0)], 10, "Grey")
    canvas.draw_polygon([(400, 400), (400, 0)], 5, "Grey")
    canvas.draw_polygon([(0, 400), (400, 400)], 5, "Grey")



## Frame
frame = simplegui.create_frame("SimpleGUI", CanvasWidth, CanvasHeight)
ScoreLabel = frame.add_label("   ")


## Init
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)
frame.set_draw_handler(draw)
frame.start()
