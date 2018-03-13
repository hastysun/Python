## Unit 4 Homework - 3 Things Turtle can do
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random
import turtle
import tkinter

## Turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")


class ToggleTurtle(turtle.Turtle):

    # This toggles between two colors when clicked

    def __init__(self):

        turtle.Turtle.__init__(self)

        # The above line lets Toggle turtle have all methods
        # And attributes of a initial turtle

        self.shape("arrow")
        self.color("black", "grey")

        # The first color sets the pen color and outline
        # The second color sets the fill color

    def ToggleColor(self, x, y):

        ColorList = self.color()
        self.color(ColorList[1], ColorList[0])

    def OriginalColor(self, x, y):

        ColorList = self.color()
        self.color(ColorList[0])


## Main
arrow = ToggleTurtle()
screen.onclick(arrow.ToggleColor)


## EOF
screen.mainloop
