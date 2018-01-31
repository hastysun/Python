## Unit 4 Lesson 1 - Classes and Objects
## Gavin Weiss - Computer Programming II

## Libraries
import time
import random
import os

## Code

# Basics of object oriented programming

# Classes and Objects are the foundation of object-oriented programming
# A class is a group that has similar functions and variables
# A class defines characteristics, and these are called attributes
# Also behaviors called methods
# From a class, you can create, or "instantiate",
# An object that uses attributes and methods from that class
# An object instantiated from the same class, will have the same attributes
# Note that objects may be referred to as instances
# Note that attributes are sometimes referred to as data fields

# Defining a class
class Critter(object):  # It is conventional to capitalize class name
    """A Virtual Pet"""  # A docstring to describe an object that can be made

    def talk(self):
    # This defines a method, methods are functions that are linked to an object
        print("\n Morning fellas, I'm an object instantiated from a class.")

# talk() has the parameter 'self'
# Every instance method (a method that every object of a class has)
# Must have a special first parameter, called 'self', by convention
# This parameter allows object to use attributes and methods from it's class

# Now let's instantiate our first object from this classes


tim_the_critter = Critter()

tim_the_critter.talk()

# Homework
# Create your own class with two methods
# Instantiate an object from that class and have it use the methods
