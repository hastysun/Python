## Unit 2 Lesson 2 - elif Statements
## Computer Programming II - Gavin Weiss

# elif stands for "else if"

# elif allows you to check for different values and will not check
# check for further conditions once it finds one that works

grade_level = raw_input("What grade are you in?")

if grade_level == "9":

    print("Welcome to the high school, freshman")

elif grade_level == "10":

    print("Sophomore, huh? Bet you're glad you're not a freshman.")

elif grade_level == "11":

    print("Welcome back, Junior.")

elif grade_level == "12":

    print("I bet you wanna get outta here Senior.")

else:

    print("You're not even in high school, get outta here.")
