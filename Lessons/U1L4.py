## Unit 1 Lesson 4 - Working With Numbers
## Computer Programming II - Gavin Weiss

# Basic operations in Python:

# X + Y - Add
# X - Y - Subtract
# X * Y - Multitply
# X ** Y - Find Power
# X / Y - Division
# X // Y - Number of whole times Y goes into X
# X % y - Give remainder when X is divided by Y
# This is called the "Modulus"
# abs(X)
# Give the absolute value

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 ** 2)
print(1 / 2)
print(1 // 2)
print(1 % 2)
print(abs(2))
print("")

# Two main types of numbers we'll use are
# Integers and floats (decimals)

# Reminder!
# User input is returned as a string
# If we want numeric value input from the User
# They must be converted into numbers

length = raw_input("What is the length of your rectangle? ")
width = raw_input("What is the width of your rectangle? ")

area = float(length) * float(width)

print("The area of your rectangle is " + str(area) + " square units.")
