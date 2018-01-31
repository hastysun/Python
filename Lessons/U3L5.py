## Unit 3 Lesson 5 - Dictionaries
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random

## Functions
def sleep():

    time.sleep(0.5)
    print("\n")
    return

# Code
# With a dictionary, you give a key and it returns a value
# Note that you cannot ask for a value, and have it return a key
# We set up a dictionary using curly braces, {}


names = {

    "Toulson, Micheal": "Age: 42, Mathematics Teacher, "
    "Lives in Cooperstown, NY", "Toulson, Molly": "Age: "
    "37, Health Teacher, Lives in Cooperstown, NY",
    "Toulson, William": "Age: 70, Retired, Lives in Vestal, NY",
    "Tillipaugh, Andrew": "Age: 40, Lawyer, Lives in Mars, PA",
    "Doe, John": "Information Unknown"

}


# There are two ways we can retrieve values from our dictionary

# Method 1
sleep()
print(names["Toulson, Micheal"])

# Method 2
sleep()
print(names.get("Doe, John"))

sleep()
print(names.get("Barber, Sean"))  # Prints "None"; not in dictionary

sleep()
print(names.keys())  # Prints all the keys in dictionary, as a list

sleep()
print(names.values())  # Prints all values in dictionary

sleep()
print(names.items())  # Prints all key value pairs

# Since these outputs are lists, we will be able to modify them
# You can add and delete information from them

# You can build a dictionary from two lists

first_names = ["Max", "Jack", "Wriley"]

last_names = ["Hinrichs", "Odell", "Nelson"]

full_names = dict(zip(first_names, last_names))
# The line above makes a dictionary that pairs corresponding items in each list

sleep()

for names in full_names.items():

    sleep()
    print(names)

sleep()
print(full_names.items())
