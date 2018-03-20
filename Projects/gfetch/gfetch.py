## gfetch - fetches system info
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import os


## Variables
HostName = os.popen("uname -n").read()
Kernel = os.popen("uname -r").read()
Battery = os.popen("acpi").read()
Architecture = os.popen("uname -m").read()


## Init
print("\n")
print("-------------------------")
print("\t \t gfetch")
print("-------------------------")
print("\n Hostname - " + HostName)
print("\n Kernel - " + Kernel)
print("\n Battery - "+ Battery)
print("\n Architecture - " + Architecture)
