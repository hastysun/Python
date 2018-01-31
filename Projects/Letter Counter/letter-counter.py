## Letter Counting Project
## Computer Programming II - Ian Thomas & Gavin Weiss

## Libraries
import time
import random

## Code

x=str(input("Please Insert a String > "))
e=0
for i in x:
   if 'e' in i:
      e=e+1
print(e)

if e == 1:
    print("There is " + str(e) + " e in what you entered.")

elif e > 1:
    print("There is " + str(e) + " e's in what you entered.")

elif e < 1:
    print("There is " + str(e) + " e's in what you entered.")
