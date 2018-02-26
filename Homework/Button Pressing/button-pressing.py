## Unit 5 Lesson 3 - Button Pressing
## Computer Programming II - Gavin Weiss


#! Homework : Be able to press a button and have text appear


## Libraries
import time
import random
import simpleguitk as simplegui


## Code

## Define Global
factor1 = 3
factor2 = 5


## Define Helper Functions



## Define Classes



## Define Event Handlers
def CalcProduct():

    global factor1, factor2
    product = factor1 * factor2
    print(product)


## Create Frame
frame = simplegui.create_frame("Product Calculator", 64, 64)



## Register Event Handlers
PrintProduct = frame.add_button("Print Product", CalcProduct)


## Start Frame and Timers
frame.start()

