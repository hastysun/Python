## Unit 3 Lesson 1 - For Loops
## Computer Programming II - Gavin Weiss

## Modules
import time

## Code

# A "for" loop is used to run through a series of code (loop body)
# A set number of times (iterations)

# The loop repeats for each element in a sequence
# When it reaches the end of the sequence, the loop ends

# Pushup Program
for pushup_count in range(1, 6):  # Used 1 - 6, starts with 6, ends with 5

    time.sleep(0.1)
    print("\nDown")

    time.sleep(0.1)
    print("\nUp")

    time.sleep(0.1)
    print(pushup_count)

    time.sleep(0.1)
    print("\n")

# Word Printer
word = "Python"

word_length = 0

for letter in word:

    time.sleep(0.1)
    print(letter)  # The elements will be printed vertically

for letter in word:

    time.sleep(0.1)

    print("\n")
    time.sleep(0.1)
    print(letter),  # The comma will print your elements horizontally

# Word Length Counter
word_length = 0

for letter in word:

    word_length = word_length + 1

time.sleep(0.1)
print("\n")

time.sleep(0.1)
print(word_length)

time.sleep(0.1)
print("\nThere are " + str(word_length) + " letters in the word " + word + ".")

# As a side note, the above loop can be summarized using the length function

time.sleep(0.1)
print("\n")

time.sleep(0.1)
print(len(word))
