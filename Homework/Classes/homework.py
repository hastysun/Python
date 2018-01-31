# Homework - Unit 4 Lesson 1 - Classes and Objects
# Gavin Weiss - Computer Programming II

# Libraries
import time
import random
import os

# Functions


def sleep():

    time.sleep(0.1)
    print("")

    return

# Code


class Robot(object):
    """A Robot"""

    def talk_0(self):
        print("Hello, my name is RX-480, and I'm a robot.")

    def talk_1(self):
        print("I can do math!")

    def talk_2(self):
        print("2 * 6 - 4 is...")

    def math(self):
        print(2 * 6 - 4)

    def talk_3(self):
        print("Have a nice day!")


robot_interface = Robot()

sleep()

robot_interface.talk_0()

sleep()

robot_interface.talk_1()

sleep()

robot_interface.talk_2()

sleep()

robot_interface.math()

sleep()

robot_interface.talk_3()

sleep()

quit()
