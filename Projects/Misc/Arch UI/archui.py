#!/usr/bin/python
## This is so Linux knows what to do with it

## Arch UI Project
## Computer Programming II - Gavin Weiss 2017

## This is a simple script made by Gavin Weiss
# The primary purpose it to automate what I usually do everyday

## Libraries
import time # For my cleanliness function
import os # For executing commands
import os, platform # Checking OS

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

def boot_time():

    os.system("systemd-analyze")
    sleep()

    return

def packages():

    os.system("pacman -Qqs | wc -l")
    sleep()

    return

## Code
sleep()
print("")
print("#######################################")
os.system("\t figlet Arch UI ")
print("#######################################")

sleep()

# Platform (OS) Checking
if platform.system() == "Windows":

    sleep()
    print("\n > Windows detected, now exiting.")

    sleep()
    quit()

if platform.system() == "Linux":

    sleep()
    print("\n > Linux detected")

else:

    sleep()
    print("\n ERROR: Could not detect OS")

    sleep()
    quit()

#sleep()
#print("\n Trimming SSD...")


#sleep()
#trim()

sleep()
print(" > Updating Pacman")

sleep()
update()

sleep()
print(" > Analyzing boot time")

sleep()
boot_time()

sleep()
print(" > Analyzing amount of installed packages")

sleep()
packages()

print("\n\a > Finished ") # \a sends a terminal bell to signal it's done
sleep()
