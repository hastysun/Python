# Gavin Weiss September 2017
# Computer Programming II Period 2
# Madlibs Project

# Libraries
import time

# Code
time.sleep(0.5)
print("v0.1")
print("\n\t           ======================================")
print("\n\t             Welcome to the worst Madlib ever...  ")
print("\n\t           ======================================")
time.sleep(0.5)

confirmation = raw_input("\nWould you like to play a Madlib? ")

if confirmation.upper() == ("YES"):
    print("\nThen get ready!")

elif confirmation.upper() == ("NO"):
    print("\nMaybe another time.")
    quit()

else:
    print("\nInvalid answer")
    quit()

time.sleep(1)
print("\nI'll assume you know how a Madlib works, if not, please type in no")
time.sleep(1)

confirmation1 = raw_input("\nAm I correct? ")

if confirmation1.upper() == ("YES"):
    time.sleep(1)
    print("\nGood.")

elif confirmation1.upper() == ("NO"):
    time.sleep(2)
    print("\nA mad lib is a classic game where the objective")
    time.sleep(2)
    print("\nIs to fill in blanks with certain types of words")
    time.sleep(2)
    print("\nTo form a funny piece of text")

else:
    print("\nInvalid Answer.")

time.sleep(1)
print("\nLet's begin.")

time.sleep(1)
mlib1 = raw_input("\nYou wake up in your : ")

print("\nNext")

time.sleep(1)
mlib2 = raw_input("\nYou get up and make some : ")

print("\nNext")

time.sleep(1)
mlib3 = raw_input("\nWhat you made was so bad you : ")

print("\nNext")

time.sleep(1)
mlib4 = raw_input("\nYou are rushed to the emergency room by a : ")

print("\nNext")

time.sleep(1)
mlib5 = raw_input("\nThe doctor takes one look at you and almost : ")

print("\nNext")

time.sleep(1)
mlib6 = raw_input("\nSuddenly a _____ flies through the window and hits you. : _")

print("\nNext")

time.sleep(1)
mlib7 = raw_input("\nIt scared you so much you decided to _____ : _ ")

print("\nNext")

time.sleep(1)
mlib8 = raw_input("\nAfter being discharged from the hospital, you go home and watch some _____ : _ ")

print("\nNext")

time.sleep(1)
print("\nYou get bored and go check the mail.")
mlib9 = raw_input("\nSomething pops out of the mailbox and _____ you. : _")

print("\nNext")

time.sleep(1)
mlib10 = raw_input("\nWhatever popped out and did to you was so bad that you _____. : _")
print("\nAnd Whatever happened was so bad that it led to your death.")

time.sleep(3)
print("\nThe results are as follows.")
time.sleep(1)
print("\n\tYou wake up in your " + mlib1 + ".")
time.sleep(1.5)
print("\n\tYou get up and make some " + mlib2 + ".")
time.sleep(1.5)
print("\n\tWhat you made was so bad that you " + mlib3 + ".")
time.sleep(1.5)
print("\n\tYou are rushed to the emergency room by a " + mlib4 + ".")
time.sleep(2)
print("\n\tThe doctor takes one look at you and almost " + mlib5 + ".")
time.sleep(2)
print("\n\tSuddenly, a " + mlib6 + " flies through the window and hits you.")
time.sleep(2)
print("\n\tIt scared you so much you decided to " + mlib7 + ".")
time.sleep(2)
print("\n\tAfter being discharged from the hospital, you go home and watch some " + mlib8 + ".")
time.sleep(3)
print("\n\tYou get bored and check the mail.")
time.sleep(1.5)
print("\n\tSomething pops out of the mailbox and " + mlib9 + " you.")
time.sleep(2.5)
print("\n\tWhat ever popped out and did to you was so bad that you " + mlib10 + ".")
time.sleep(2.5)
print("")
time.sleep(1)
print("")
time.sleep(1)    # These blanks are for dramatic effect
print("")
time.sleep(1)
print("")
time.sleep(1)
print("")
time.sleep(1)
print("")
time.sleep(1)
print("\n\tAnd Whatever Happened Led To Your Death...")
time.sleep(1)
print("\n\tThank you for playing!")
quit()
