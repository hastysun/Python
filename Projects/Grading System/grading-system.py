###############################################
###          Grading Sytem 9000             ###
###############################################
## Gavin Weiss 2017 Computer Programming II
## Due Tuesday, October 10th

## Modules
import time # For timing and cleanliness

## Variables

    # weight_TA - Test Average
    # weight_RP - Research Project
    # weight_CP - Class Participation
    # weight_FE - Final Exam
    # test1 - Grade for First Test
    # test2 - Grade for Second Test
    # test3 - Grade for Third Test
    # grade_RP - Grade for the Research Project
    # grade_CP - Grade for Class Participation
    # grade_FE - Grade for Final Exam
    # a_grade_TA - Average Grade for the three tests
    # a_grade_RP - Average Grade for the Research Project
    # a_grade_CP - Average Grade for Class Participation
    # a_grade_FE - Average Grade for Final Exam
    # a_grade - Final Grade
    # total_weight - Total Weight

## Code
time.sleep(0.5)
print("\n\tWelcome to the Grading System 9000")

time.sleep(0.5)
print("\nThis program is to calculate grades with weights.")

time.sleep(1)
print("\nThe categories are: ")

time.sleep(2)
print("\n - Test Averages")

time.sleep(1)
print("\n - Research Project")

time.sleep(1)
print("\n - Class Participation")

time.sleep(1)
print("\n - Final Exam")

time.sleep(1)
print("\nNext, please enter the weights for each category.")

time.sleep(1)
print("\nPlease enter the weight for the Test Average.")

weight_TA = float(raw_input("> "))

time.sleep(0.5)
print("\nThe weight for Test Average is set to " + str(weight_TA) + "%.")

time.sleep(0.7)
print("\nNext, please enter the weight for a Research Project.")

weight_RP = float(raw_input("> "))

time.sleep(0.5)
print("\nThe weight for a Research Project is set to " + str(weight_RP) + "%.")

time.sleep(0.7)
print("\nNext, please enter the weight for Class Participation.")

weight_CP = float(raw_input("> "))

time.sleep(0.5)
print("\nThe weight for Class Participation is set to " + str(weight_CP) + "%.")

time.sleep(0.7)
print("\nLastly, please enter the weight for the Final Exam.")

weight_FE = float(raw_input("> "))

time.sleep(0.5)
print("\nThe weight for Final Exam is set to " + str(weight_FE) + "%.")

time.sleep(1)
print("\nNext, please enter the data for the Grades.")

time.sleep(0.5)
print("\nPlease enter the grades for the 3 tests.")

time.sleep(0.7)
print("\nPlease enter the grade for the first test.")

test1 = float(raw_input("> "))

time.sleep(0.5)
print("\nPlease enter the grade for the second test.")

test2 = float(raw_input("> "))

time.sleep(0.5)
print("\nPlease enter the grade for the third test.")

test3 = float(raw_input("> "))

time.sleep(1)
print("\nNow, please enter the grade for the Research Project.")

grade_RP = float(raw_input("> "))

time.sleep(1)
print("\nNow please enter the grade for Class Participation.")

grade_CP = float(raw_input("> "))

time.sleep(1)
print("\nNow, please enter the grade for the Final Exam.")

grade_FE = float(raw_input("> "))

time.sleep(1)
print("\nThe weights are set and the grades are entered")

time.sleep(1)
print("\nThe current values are as follows.")

time.sleep(0.5)
print("\nWeights :") # Summary of the Weights that are set

time.sleep(1)

time.sleep(0.5)
print("\n - Test Average Weight = " + str(weight_TA) + "%.")

time.sleep(0.5)
print("\n - Research Project Weight = " + str(weight_RP) + "%.")

time.sleep(0.5)
print("\n - Class Participation Weight = " + str(weight_CP) + "%.")

time.sleep(0.5)
print("\n - Final Exam Weight = " + str(weight_FE) + "%.")

time.sleep(0.1)
print("\n")
time.sleep(0.1)
print("\n")

time.sleep(1)
print("\nThe Grades that were entered are as follows.")

time.sleep(0.5)
print("\n - Test Averages are :")

time.sleep(0.5)
print("\n   - Test 1 = " + str(test1) + "%.")

time.sleep(0.5)
print("\n   - Test 2 = " + str(test2) + "%.")

time.sleep(0.5)
print("\n   - Test 3 = " + str(test3) + "%.")

time.sleep(1)
print("\n - Research Project is a " + str(grade_RP) + "%.")

time.sleep(1)
print("\n - Class Participation is a " + str(grade_CP) + "%.")

time.sleep(1)
print("\n - Final Exam is a " + str(grade_FE) + "%.")

time.sleep(1)
print("\nIf there are any errors, please restart the program.")

time.sleep(0.5)
print("\nNow that all grades are entered, the calculation process can begin.")

# Math for the Calculated Average of all three tests
a_grade_TA = (test1 + test2 + test3) / 3

# Math for Total Weight
total_weight = weight_CP + weight_FE + weight_RP + weight_TA

# Math for Final Grade
a_grade = (a_grade_TA * weight_TA + grade_CP * weight_CP + grade_RP * weight_RP + grade_FE * weight_FE) / total_weight

time.sleep(0.5)
print("\n\tThe grade for all is " + str(a_grade) + "%.")

if a_grade >= (94):

    time.sleep(0.5)
    print("\nThe student received an A.")

elif a_grade < (94) and a_grade >= (90):

        time.sleep(0.5)
        print("\nThe student received an A-.")

elif a_grade < (90) and a_grade >= (87):

    time.sleep(0.5)
    print("\nThe student received an B+.")

elif a_grade < (87) and a_grade >= (84):

    time.sleep(0.5)
    print("\nThe student received an B.")

elif a_grade < (84) and a_grade >= (80):

    time.sleep(0.5)
    print("\nThe student received an B-.")

elif a_grade < (80) and a_grade >= (77):

    time.sleep(0.5)
    print("\nThe student received an C+.")

elif a_grade < (77) and a_grade >= (74):

    time.sleep(0.5)
    print("\nThe student received an C.")

elif a_grade < (74) and a_grade >= (70):

    time.sleep(0.5)
    print("\nThe student received an C-.")

elif a_grade < (70) and a_grade >= (67):

    time.sleep(0.5)
    print("\nThe student received an D+.")

elif a_grade < (67) and a_grade >= (64):

    time.sleep(0.5)
    print("\nThe student received an D.")

elif a_grade < (64) and a_grade >= (60):

    time.sleep(0.5)
    print("\nThe student received an D-.")

elif a_grade < (60):

    time.sleep(0.5)
    print("\nThe student received an F.")


# Just for effect
time.sleep(0.1)
print("\n")

time.sleep(0.1)
print("\n")

time.sleep(0.1)
print("\n")

time.sleep(0.1)
print("\n")

time.sleep(0.1)
print("\n")

time.sleep(1)
print("\n\tThank You For Using the Grading System 9000")

time.sleep(0.1)
print("\n\tPlease email hasty459@gmail.com for questions or concerns.")
