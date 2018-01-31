## Lookup Program Project
## Computer Programming II - Gavin, Ian, Wriley, Blake, Jack

## Libraries
import random
import time

## Functions
def sleep():

    time.sleep(0.5)
    print("\n")
    return

sleep()
print("\n - Welcome to the NLS v1 - ")
sleep()

password = ("")

while password !=("root"):


    password = input("\n Please enter your password : ")

    if password !=("root"):

        sleep()
        print("\n\t****ACCESS DENIED*****")
        sleep()
        quit()

    sleep()
    print("\n\t****ACCESS GRANTED****")

names = {
        "Weiss, Gavin" : "Age: 15, Linux Enthusiast, Lives in NY",
        "Doe, John" : "Age: null, Occupation: null, Lives in null"
        }

def menu():

    sleep()
    print("\n - Welcome to the name lookup system - ")

    sleep()
    print("\t - MENU - ")

    print("\n 0 - Quit") # Purposely left out a time.sleep

    time.sleep(0.1)
    print("\n 1 - Look up Person's info ")

    time.sleep(0.1)
    print("\n 2 - Add Person ")

    time.sleep(0.1)
    print("\n 3 - Delete a Person ")

    time.sleep(0.1)
    print("\n 4 - Edit a Person's info ")

    time.sleep(0.1)
    print("\n 5 - View list of all People ")

    time.sleep(0.1)
    print("\n")

    return

menu()

choice = input("=> ")

if choice ==("0"):

    sleep()
    print("\n Exiting...")

    sleep()
    quit()

if choice ==("1"):

    sleep()
    print("\n What name would you like to lookup?")

    sleep()
    print("\n Here are the current names, ")

    sleep()
    print(names.keys())

    name_request = input("=> ")

    if name_request ==("Weiss, Gavin"):

        sleep()
        print(names.get("Weiss, Gavin"))

        sleep()

    if name_request ==("Doe, John"):

        sleep()
        print(names.get("Doe, John"))

if choice ==("2"):

        print("\n Please enter the name of the person you would like to add")
        sleep()

        add_person = input("=> ")

        add_person_list = [add_person]

        added_person = dict(zip(add_person_list, names))

        for names in added_person.items():

            sleep()
            print(added_person)

if choice ==("3"):

        sleep()
        print("\n Please enter the name of the person you would like to delete")

        sleep()
        print("\n Here are the current names, ")

        sleep()
        print(names.keys())
        sleep()

        delete_person = input("=> ")

        delete_person_list = [delete_person]

        delete_person_list.remove = [delete_person]

        deleted_person = dict(zip(names, delete_person_list))

        for names in deleted_person.items():

            sleep()
            print(deleted_person)

        quit()

if choice ==("4"):

        sleep()
        print("\n Add Feature in")

if choice ==("5"):

        sleep()
        print("\n Here is a list of all of the people ")

        sleep()
        print(names)

        sleep()
        quit()
