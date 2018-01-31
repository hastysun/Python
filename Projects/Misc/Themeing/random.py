## Themeing using Pywal
## Computer Programming II - Gavin Weiss

## Libraries
import time
import random
import os
import pywal

## Functions
def sleep():

    time.sleep(0.1)
    print("")

    return

## Code
sleep()
print("\n Generating Random Theme")
sleep()

def theme():

    image = pywal.image.get("/home/gavin/Pictures/Wallapers/Concepts/")

    colors = pywal.colors.get(image, notify=True)

    pywal.sequences.send(colors)

    pywal.reload.i3()

    return

theme()
