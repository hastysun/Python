## Unit 2 Lesson 1 - Conditionals
## Computer Programming II - Gavin Weiss

# Branching is a fundamental part of computer programming
# Means making a decision to choose one path or another

# Through "if" statements, your code can branch to a section of code
# Or skip it

# All "if" statements have a condition which is true or false

# Conditions are often created by comparing values

# The following is a list of comparison operators:

#    "==" if is equal to
#    "=" is equal to
#    "!=" is not equal to
#    ">" is greater than
#    "<" is lesser than
#    ">=" greater than or equal to
#    "<=" less than or equal to

# Example
username = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")

# Adding .upper() makes it non-case sensitive
if password.upper() == "PASSWORD":

    print("\n\n\t\t ***  Acces Granted  ***")
    print("\nGoodmorning, " + username + ". Shall we play a game?")

else:

	print("\n\n\t\t *** Acces Denied ***")

# Nested "if" statements

dragon_fight = raw_input("Do you want to fight the dragon? ")

if dragon_fight.upper() == "YES":
    
	weapon = raw_input("What weapon do you want to use? ")

if weapon.upper() == "MAGIC SWORD":

	print("You slay the mighty dragon with your Magic Sword.")

else:
    
	print("\n" "The" + weapon + "does not work against the dragon.")

else:
    
		print("You run from the dragon and was never seen again")
