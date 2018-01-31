## Old Concepts


##################################
print("\nAre you Male or Female?")
time.sleep(1)

print("\nThis information will not affect gameplay,")
time.sleep(1)

print("\nIt is simply for personalization.")
time.sleep(1)

print("\n1 - Male")
print("\n2 - Female")

gender = raw_input("> ")

if gender == "1":
    time.sleep(0.5)
    print("\nThank you for answering, please continue.")
if gender == "2":
    time.sleep(0.5)
    print("\nThank you for answering, please continue.")

##################################
print("\n- Please keep the following things in mind")
time.sleep(3)
print("\n- Read all text carefully ")
time.sleep(2)
print("\n- Most answers will use a number which you input for an answer")
time.sleep(2)
print("\n- If you make one wrong choice, you die and the game restarts")
##################################
time.sleep(1)
print("")
print(
    "You are currently at the peak of a mountain in the middle of a forest, try to survive."
)
time.sleep(2)
print("\nYou can see many things from this point.")
time.sleep(2)
print("\nYou first notice two trails.")
time.sleep(2)
print("\n1 - One appears to lead to a river going east.")
time.sleep(2)
print("\n2 - The other appears to lead to a group of decayed structures due east.")
time.sleep(2)
print("\nWhich shall you choose?")

trailchoice = raw_input("> ")

if trailchoice == "1":
    print("\nYou trip on a rock and fall down the entire mountain.")
    time.sleep(1)
    print("\nYou end up getting impaled by a stick.")
    time.sleep(1)
    print("\nGame Over")
    quit()

if trailchoice == "2":
    print("\nYou start the hike towards the ruins.")

time.sleep(1)
print(
    "\nYou're walking when suddenly you hear the faint sound of something up above."
)
time.sleep(3)
print("\nA skilled archer has you lined up in his sights itching to fire.")
time.sleep(3)
print("\nHe's waiting for you to speak.")
time.sleep(2)
print("\nWhat do you say?")
time.sleep(1)
print("\n1 - Please don't kill me!")
time.sleep(0.5)
print("\n2 - If you're gonna shoot, don't miss.")
time.sleep(0.5)

archerchoice = raw_input("> ")

if archerchoice == "1":
    print(
        "\nThe archer pitys your beg for mercy and spares your life."
    )
    time.sleep(0.5)

if archerchoice == "2":
    print(
        "\nThe archer admires you're cocky bravery and spares your life, while silently laughing to himself."
    )
    time.sleep(1)
    print("\nHe tells you to meet up for some a pint of ale sometime.")

time.sleep(2)
print(
    "\nAfter a near death situation, you find a rock to sit on and drink something refreshing."
)
time.sleep(2)
print("\nWhat do you choose to drink?")
time.sleep(0.5)
print("\n1 - Drink from canteen")
print("\n2 - Drink rainwater from a hole in the rock")

drink = raw_input("> ")

if drink == "1":
    print(
        "Due to your canteen being so old, a mold developed inside of it and poisened you resulting in your death."
    )
    time.sleep(0.5)
    print("\n\tGame Over" + name + ".")
    quit()

if drink == "2":
    print("\nThe rainwater appears to be fresh surprisingly.")
    time.sleep(0.5)
    print("\nNow being rehydrated, you are ready to keep continue hiking down.")

time.sleep(1)
print("\nYou get closer to the ruins, you reach a bridge.")
time.sleep(1)
print("\nAfter passing the bridge you reach a half destroyed gate")
time.sleep(1)
print("\nYou're walking into the abandoned town when something happens.")
time.sleep(1.5)
print("\nYou accidentaly step on a trip mine.")
time.sleep(1)
print("\nYou're foot is on it, if you move, it will go detonate, resulting in a particulary bloody death.")
time.sleep(1)
print("\nWhat do you do?")
time.sleep(1)
print("\n1 - Call for help.")
time.sleep(0.5)
print("\n2 - Take a closer look at it.")
mine_answer = raw_input("> ")
if mine_answer == "1":
    print("\nYou call for help")
    time.sleep(0.5)
    print("\nYou see the archer that you recently encountered.")
    if archerchoice == "1":
        print("\nThe archer will not spare your life a second time.")
        quit()
    if archerchoice == "2":
        print("\nThe archer rememebers you and decides to help.")
