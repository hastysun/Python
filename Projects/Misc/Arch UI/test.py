#!/usr/bin/env python  ## This is so Linux knows what to do with it

## Arch UI Project
## Computer Programming II - Gavin Weiss 2017

## This is a simple script made by Gavin Weiss
# The primary purpose it to automate what I usually do everyday

## Libraries
import time # For my cleanliness function
import os # For executing commands
import os, platform # Checking OS
import sys # Not sure what this will be used for

## Functions
def sleep():

    time.sleep(0.1)
    print("\n")
    return

def trim():

    os.system("sudo fstrim -v /") # Linux Command for trimming SSD
    sleep()

    return

def update():

    os.system("sudo pacman -Syu") # (Arch) Linux Command for update
    sleep()

    return

## Code
sleep()
print("\n\t - Running Gavin's Arch Linux Maintenence Utility - ")

# Platform (OS) Checking
if platform.system() == "Windows":

    sleep()
    print("\n Windows detected, now exiting.")

    sleep()
    quit()

if platform.system() == "Linux":

    sleep()
    print("\n Linux detected")

else:

    sleep()
    print("\n ERROR: Could not detect OS")

    sleep()
    quit()

for

sleep()
print("\n Trimming SSD...")


sleep()
trim()

sleep()
print("\n Updating Arch")

sleep()
update()

print("\n\t\a - Finished - ") # \a sends a terminal bell to signal it's done
sleep()
