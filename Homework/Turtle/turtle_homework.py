##############
## Homework ##
##############

## Figure out how this works

## Unit 4 Lesson 4 - Turtle Lesson 2
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
        self.color(
					ColorList[1], 
					ColorList[0]
					)


	## Explanation for the above code
 	
	# "def ToggleColor(self, x, y):"
 
 		# This defines a function called "ToggleColor"
		
		# In parentheses,

			# "self" gets values from the ToggleTurtle class
			# "x", is the position of the turtle for the x axis
			# "y", is the position of the turtle for the y axis

		# "ColorList" creates a list for the colors
			
			# "self.color()" sets the color from "self"
			# Which again, are the default values
			# Therefore, "self" is "turtle.color"

		# "self.color(ColorList[1], ColorList[0])

			# "self.color()" is the turtle color
			# What is inside the parenthesiss, is a tuple

			# Arrays start at 0 "This is controversial"
			
			# "ColorList[1]"

				# "ColorList" comes from  the function above it
				# The values are "black" and "grey"
				# The "[1]" is the second index of "ColorList"
				# It is an index because "ColorList" is an array

					
			# "ColorList[0]"

				# "ColorList" comes from the function above it
				# The "[0]" also uses the values from line 34
				# The "[0]" is the first index of "ColorList"
				# Again, it is an index of the array "ColorList"
			

## Main 
arrow = ToggleTurtle()
screen.onclick(arrow.ToggleColor)


## End of File
screen.mainloop()
      
