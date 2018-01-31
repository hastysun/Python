# Homework from Gavin Weiss to Mr. Toulson second period CPII
# Part Invitation

# Libraries
import time

# Main
time.sleep(0.5)
print("\n")
time.sleep(0.5)
print("\n\t - Welcome to the digital Invitation for the 2017 Python Party - ")
time.sleep(0.5)
print("\n")
time.sleep(2)
print(" - Some basic infortmation for the party are as follows.")
time.sleep(2)
print("\n The date is Janurary 16th.")
time.sleep(2)
print("\n The party will begin at 6:30 PM.")
time.sleep(2)
print("\n It will be held at 123 Sesame Street.")
time.sleep(2)
print("\n - Please fill out some basic info")
time.sleep(2)
print("\n May I have your name?")
name = raw_input()
time.sleep(1)
print("\nThank you for answering " + name + ".")
time.sleep(1)
print("\nWill you be bringing anything?")
time.sleep(0.5)
print("\nPlease answer Yes or No.")
answer = raw_input()
if answer == "Yes":
    print("Thank you " + name + ".")
    time.sleep(0.5)
if answer == "No":
    print("That's okay, " + name + ".")
    time.sleep(0.5)
print("Here is a summary of the party below, " + name + ".")
time.sleep(1)
print("\n\t Date : Janurary 16")
time.sleep(1)
print("\n\t Time : 6:30 PM.")
time.sleep(1)
print("\n\t Address : 123 Sesame Street")
time.sleep(1)
print("Are you still sure you can come?")
time.sleep(1)
print("\nPlease answer Yes or No.")
confirmation = raw_input()
if confirmation == "Yes":
    time.sleep(0.5)
    print("Great! Can't wait to see you there, " + name + ".")
    quit()
if confirmation == "No":
    time.sleep(0.5)
    print("That's too bad," + name + ".")
    quit()
