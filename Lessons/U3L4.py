## Unit 3 Lesson 4 - Lists
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random

## Code

# How to convert a list to a string
# Example :

# num_list = [2,4,3,8]
# converted_str = "".join(map(str,num_list))
# converted_str = 2438


# The difference between tuples and lists is that a tuple is unchangeable
# While a list is changeable
# In terms of syntax, tuples use () while lists use []

prog_class = ["Pierce", "Jon", "Wriley", "Blake", "Ian", "Gavin"]

# A position index is the location of the item in a list

time.sleep(0.5)
print(prog_class[0])  # Prints the item in position 0

time.sleep(0.5)
print("\n")

time.sleep(0.5)
print(prog_class[-1])

time.sleep(0.5)
print("\n")

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

time.sleep(0.5)
print("\n\tNext List - Replaced Name")

time.sleep(0.5)
print("\n")

# You can change the value of elements in the list

prog_class[2] = ("Hercules")  # Replaces the value in second position

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

# You can find the position index for an element using .index

time.sleep(0.5)
print(prog_class.index("Gavin"))  # This returns the value of the index

# We can sort the elements in our lists using .sort
# This will sorts the values from highest to lowest
# Or it can list strings alphabetically

time.sleep(0.5)
print("\n\tNext List - Alphabetical")

time.sleep(0.5)
print("\n")

prog_class.sort()

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

# We can do a reverse sort using .sort(reverse = True)

time.sleep(0.5)
print("\n\tNext List - Reverse Order")

time.sleep(0.5)
print("\n")

prog_class.sort(reverse=True)

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

#! We can add an element to the list using .append

prog_class.append("Max")  # This adds a new element to the end of the list

time.sleep(0.5)
print("\n\tNext List - Appended Name")

time.sleep(0.5)
print("\n")

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

# We can remove an element from a list using .remove

prog_class.remove("Max")

time.sleep(0.5)
print("\n\tNext List - Removed Element")

time.sleep(0.5)
print("\n")

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")

# If you remove an element, it will only remove the first instance

# You can use the len function to count the total number of elements

time.sleep(0.5)
print(len(prog_class))

time.sleep(0.5)
print("\n")

# We can concatenate two lists

more_names = ["Max", "Jon's Mom", "Carson", "Loki"]

time.sleep(0.5)
print("\n\tNext List - Combined list")

time.sleep(0.5)
print("\n")

prog_class += more_names  # Concatenates the two lists together

for names in prog_class:

    time.sleep(0.2)
    print(names)

    time.sleep(0.5)
    print("\n")
