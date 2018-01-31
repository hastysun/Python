## Unit 2 Lesson 3 - Booleans, Compound Statements, Random Module, Time Modules
## Computer Programming II - Gavin Weiss

## Modules
import random
import time

## Code

# Boolean operators:
# and
# or
# not

a = 5
b = 11

print(a == b)
print(a <= b)
print(a > 3 and b < 20)
print(a > 10 or b < 20)
print(not(a < 10))

# We must be careful because there is an "order of operations"
# For boolean expressions.
# 'and' statements are done before 'or' statements.
# You can use parentheses to indicate the order you want

print(a > 0 or b > 7 and b < 10)
print((a > 0 or b > 7) and b < 10)

# Random
roll_die = random(1, 6)
print(roll_die)

# Time
time.sleep(5)
print("Time to wake up!")
