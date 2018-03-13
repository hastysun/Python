##############################################################
### Galactia : A text adventure game coded by Gavin Weiss. ###
##############################################################

## The name "Galactia" is subject to change.
## See credits.py for the list of credits and people who have helped so far.
## This code is free to use, all I ask is proper credit

## Additional Notes
# I get many weird errors if I use "input()" rather than "raw_input()"

## Credits
# Gavin Weiss
# Contact me at hasty459@gmail.com

## Alpha and Beta Testers
# Peter Sillaro - psillaro@ccsmail.org

## Modules
import time # The time module is for timing to get cleaner code
import sys # May not be used
import random # The random module is for randomization

## Code
time.sleep(0.1)
print("\n\t")
time.sleep(0.1)
print("\t<>-=====================-<>")
time.sleep(0.1)
print("\t     -< Galactia 0.1 >-      ") # Add more intracate title
time.sleep(0.1)
print("\t<>-=====================-<>")
time.sleep(0.1)
print("\t")

time.sleep(2)
print("\n")
print("\nLet's start with your name shall we? ")

# I plan on making the name Gavin have "developer mode"
# Also maybe a different experiance for different names

print("\n")

name = raw_input("> ")

if name.upper() == "GAVIN":

    time.sleep(1)
    print("\nWelcome, Game Master")

elif name.upper() == "TOULSON":

    time.sleep(1)
    print("\nWelcome, Teacher")

elif name.upper() == "NULL":

    time.sleep(1)
    print("\nYou have chosen the forbidden name...")

    time.sleep(1)
    print("\n")

    time.sleep(1)
    quit()

else:
    time.sleep(1)
    print("\nWelcome, " + name)

time.sleep(1.5)
print("\nAre you ready for an adventure?")
time.sleep(0.5)

print("\n1 <> Yes")
print("\n2 <> No")

time.sleep(0.1)
print("\n")
time.sleep(0.1)

answer1 = raw_input("> ")

if answer1 == "1":

    print("\nThen let's begin...")
    time.sleep(1)

if answer1 == "2":

    time.sleep(0.5)
    print("\nAnother time perhaps")

    time.sleep(0.5)
    print("\n")

    time.sleep(1)
    quit()

time.sleep(1)
print("\n\t\tRemember " + name + ", every answer is life or death.")
time.sleep(2)

time.sleep(1)
print("\nThrown into action!")
time.sleep(1.5)

print("\nYou encounter a feral animal on the planet you're scanvenging.")
time.sleep(1.5)

print("\nWhat do you do?")
time.sleep(1.5)

print("\n1 - Use stun baton, and attack head on.")
time.sleep(1)

print("\n2 - Quick draw your blaster and fire.")
time.sleep(1)

time.sleep(0.1)
print("\n")
time.sleep(0.1)

animal = raw_input("> ")

animal1 = random.choice('ab')

if animal == "1":

    if  animal1 == "a":

        print("\nYou successfully slay the animal.")
        time.sleep(0.5)

    elif animal1 == "b":

        print("\nYou trip and mess up your swing, resulting in your death.")
        time.sleep(1)

        print("\n\tGame Over, " + name + ".")
        time.sleep(0.5)

        print("\n")
        time.sleep(0.5)

        quit()

animal2 = random.choice("ab")

if animal == "2":

    if  animal2 == "a":

        print("\nYou line up your shot and fire dead on, the animal is disintegrated.")
        time.sleep(1)

    elif  animal2 == "b":

        print("\nYou prime your blaster but lose your balance and miss your shot.")
        time.sleep(1.5)

        print("\nYou get trampled and slaughtered.")
        time.sleep(1.5)

        print("\n\tGame Over, " + name + ".")
        time.sleep(0.5)

        print("\n")
        time.sleep(0.5)

        quit()

    else:
        print("Error")
        quit()

time.sleep(0.5)
print("\n")

time.sleep(1)
print("\n\tYou walk back to your spaceship to leave this mortal world.")

time.sleep(0.5)
print("\n")

time.sleep(1)
print("\nWhat planet would you like to fly to?")
time.sleep(1)

time.sleep(1)
print("\n1 <> Planet 99-HG")
print("2 <> The Sun")
print("\n")

planet_choice = raw_input("> ")

time.sleep(1)

planet_choice_1 = random.choice("a,b")

if planet_choice == "1":

    if  planet_choice_1 == "a":
        time.sleep(1)
        print("\nYou kick your ship into hyper drive.")
        time.sleep(1)
        print("\nYou arive at Planet 99-HG successfully without a hitch.")

    if  planet_choice_1 == "b":
        time.sleep(1)
        print("\nYou start flying into orbit, it's quiet. ")

        time.sleep(1)
        print("\nToo quiet...")

        time.sleep(1)
        print(


            "\nUnfortunately, a planet was doing missle testing, "
            "\n"
            "\nA nuclear missle flew directly into your ship resulting in your death."
        )
        time.sleep(3)

        print("\n\tGame over, " + name + ".")
        time.sleep(0.5)

        quit()

    elif planet_choice == "2":
        print("\nWhy would you fly into the sun?")
        time.sleep(1)
        print("\n\tGame over, " + name + ".")
        time.sleep(0.5)
        print("\n")
        time.sleep(1)
        quit()

time.sleep(1)

print("\nYou enter the orbit of Planet 99-HG, navigating to the nearest outpost.")
time.sleep(1)

print("\nYou start heading towards Outpost A64-Alpha.")
time.sleep(1)

print("\nYou initiate the landing seqeunce, and land at landing pad 3.")
time.sleep(1)

print("\nYou get out of your ship, only to be at gunpoint.")
time.sleep(1)

print("\nYou completely forgot about the debt you owe...")
time.sleep(1)

print("\nXaxar The Murderous and his 2 followers are in front of you.")
time.sleep(1)

print("\nYou're clearly outnumberd and outgunned.")
time.sleep(1)

print("\nWhat do you do?")
time.sleep(1)

print("\n1 <> Say: I'll go get the money, it's in my ship.")
time.sleep(0.5)

print("\n2 <> Say: You know I don't have the money Xaxar.")
time.sleep(0.5)

xaxar_random = random.choice("a,b")

xaxar = raw_input("> ")

if xaxar == "1":

    time.sleep(1)
    print("\nYou're in your ship, now what?")

    time.sleep(1)
    print("\n1 <> Search for money.")

    time.sleep(1)
    print("2 <> Fire your ship's guns and kill them.")

    xaxar_ship = raw_input("> ")

    if xaxar_ship == "1":

            time.sleep(1)
            print("\nYou don't find anything.")
            time.sleep(1)
            print("\nXaxar comes in and kill you.")
            time.sleep(1)
            print("\n\tGame over, " + name + ".")
            time.sleep(1)
            quit()

    if xaxar_ship == "2":

            if xaxar_random == "a":

                time.sleep(1)
                print("\nYou tried to kill them with your ship guns.")
                time.sleep(1)
                print("\nYour ships's lasers melted from an ammo miscalculation and they killed you first.")
                time.sleep(1)
                print("\n\tGame over, " + name + ".")
                time.sleep(0.5)
                quit()

            if xaxar_random == "b":

                time.sleep(1)
                print("\nYou attempted to fire your ship guns at them.")
                time.sleep(1)
                print("\nThey are dead and riddled with holes.")
                time.sleep(1)

time.sleep(1)
print("\nSomehow you escaped debt from Xaxar The Murderous")

time.sleep(1)
print("\nThis will certainly boost your fame.")

time.sleep(1)
print("\nWhat now?")

time.sleep(0.5)
print("\n1 <> Refuel your ship and go back into orbit.")

time.sleep(0.5)
print("2 <> Explore the Planet.")

choice1 = raw_input("> ")

if choice1 == "1":

    time.sleep(0.5)
    print("\nYou go to refuel your ship, but the oupost is all out.")

    time.sleep(0.5)
    print("\nIn fact, there's no one even here, this certainly is odd.")

    time.sleep(0.5)
    print("\nGuess you'll have to find some natural resources on the Planet.")

if choice1 == "2":

    time.sleep(0.5)
    print("\nYou gather supplies from your ship, then lock it up.")

    time.sleep(0.5)
    print("\nYou get your survival gear and suit on, and set out")

time.sleep(0.5)
print("\nYour ship now has no fuel, you decide to explore the planet.")

time.sleep(3)
print("\nYou could either explore the planet for fuel, or for curiosity.")

time.sleep(2)
print("\nEither way, you start heading North.")

time.sleep(0.5)
print("\nThere are two main sights to follow")

time.sleep(0.5)
print("\nYou can either head towards what looks like a radiation anomaly,")

time.sleep(1)
print("\nAre what looks like an abandoned ship storage facility.")

time.sleep(0.5)
print("\nWhich do you choose?")

direction = raw_input("> ")

time.sleep(0.5)
print("\n1 <> Radiation Anomaly")

time.sleep(0.5)
print("2 <> Ship Storage Facility")

if direction == "1":

    time.sleep(0.5)
    print("\nYou head to the radiation anomaly.")

    time.sleep(0.5)
    print("\nYou hear a beeping sound...")

    time.sleep(0.5)
    print("\nYour suit's radiation cleansing system fails.")

    time.sleep(0.5)
    print("\nIt gets harder to breath and your lungs flood with gaseous radiation.")

    time.sleep(1)

    time.sleep(0.5)
    print("\n\tGame over, " + name + ".")

    time.sleep(0.5)
    quit()

if direction == "2":

    time.sleep(0.5)
    print("\nYou get walk to what seeems like a side door to the giant warehouse.")

time.sleep(0.5)
print("\nThere's a lock, but it's rusted. A good heel kick will break it off.")

time.sleep(0.5)
print("\nYou drive your heel into the door, right next to the lock.")

time.sleep(0.5)
print("\nIt flies open and slams against the wall.")

time.sleep(0.5)
print("\nThe sound echoes througouht the entire warehouse.")

time.sleep(0.5)
print("\n\tYou get the empty feeling of this place, theres wind blowing through the broken windows.")

time.sleep(0.5)
print("\n\tThe entire facility is covered in dust.")

time.sleep(0.5)
print("\nThe facility has a ton of ships, but of course they're all picked clean of parts.")

time.sleep(0.5)
print("\nIt's thousands of years old so this isn't surprising.")

time.sleep(0.5)
print("\nYou decide to go down to the basement, there might be fuel in the backup generators.")

time.sleep(0.5)
print("\nCertainly something other scavengers wouldn't have thought of.")

time.sleep(0.5)
print("\nYou find your way to the basement, all sorts of weird plants have grown everywhere.")

time.sleep(0.5)
print("\nYou go through the door, the entire structure creaks and settles.")

time.sleep(0.5)
print("\nYou focus on your main objective, to find fuel.")

time.sleep(0.5)
print("\nThe urge to explore is to strong...")

time.sleep(0.5)
print("\nTheres a circuit box near the entrance.")

time.sleep(0.5)
print("\nDo you want to try to restore the power?")

time.sleep(0.5)
print("\n1 <> Yes")

time.sleep(0.5)
print("2 <> No")

power = raw_input("> ")

if power == "1":

    time.sleep(0.5)
    print("You pry the door off the circuit box.")

    time.sleep(0.5)
    print("It breaks right off.")

    time.sleep(0.5)
    print("You see a big red switch and flip it.")

    time.sleep(0.5)
    print(".")

    time.sleep(0.5)
    print(".")

    time.sleep(0.5)
    print(".")

    time.sleep(0.5)
    print("It spews sparks everywhere, and stutters.")

    time.sleep(0.5)
    print("Nothing happens...")

if power == "2":

    time.sleep(0.5)
    print("You assume it probably won't work anyway.")

time.sleep(0.5)
print("You continue your search for fuel.")

time.sleep(0.5)
print("You find the generator, it has a barely working battery powered light over it.")

time.sleep(0.5)
print("The generator's fuel tank is empty.")

time.sleep(0.5)
print("Luckily, theres a spare container of fuel to the side of it.")

time.sleep(0.5)
print("You bring it with you.")
