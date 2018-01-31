## Unit 1 Lesson 3 - Variables
## Computer Programming II - Gavin Weiss

# We can write our variables in different styles
# You should be consistent within your program

# Example of a good variable names :
# first_name
# firstName

# FirstName
# firstname

# Best to keep variable names short
# Variable can NOT start with a number

FirstName = "Gavin"
print(FirstName)

print("Hello, " + FirstName)

print("Hello, " + FirstName + ". " + "How are you?")

# name = input ("What is your name?")
# print ("Hello " + name)

# The return value of an input function is a string
# This is important for numbers

# We can use string methods to vary how our strings look

# You invoke, or start, a method using a dot
# Methods are similiar to functions
# Except they cannot be called on their own
# A string method must be called through a particular string

print("\n" * 2)

print(FirstName.upper())
print(FirstName.upper())
print(FirstName.capitalize())

print(FirstName.count("G"))
# Gives the position or index of the letter
# Counting in programming always starts with 0

print(FirstName.replace('a', 'n'))

# HOMEWORK:

# Write a party invitation program where the user inputs information
# About the party and the program outputs information about the party

# The invitation must include:
# Name of the host
# Time, date, place
# And any other relevant information

# Worth ten points
