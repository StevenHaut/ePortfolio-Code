# Defines the function "main".
def main():
    # Asks user for 5 test scores.
    print("Enter 5 test scores: ")
    # Variable "test1" is assigned the entered float value, then passed
    # to the "test_average" function.
    test1 = float(input("Test 1: "))
    # Variable "test2" is assigned the entered float value, then passed
    # to the "test_average" function.
    test2 = float(input("Test 2: "))
    # Variable "test3" is assigned the entered float value, then passed
    # to the "test_average" function.
    test3 = float(input("Test 3: "))
    # Variable "test4" is assigned the entered float value, then passed
    # to the "test_average" function.
    test4 = float(input("Test 4: "))
    # Variable "test5" is assigned the entered float value, then passed
    # to the "test_average" function.
    test5 = float(input("Test 5: "))
    # The variable "score_average" is assigned the return value from the function "calc_score average".
    # Calls the "calc_score_average" function, passed with the arguments "test1-test5".
    score_average = calc_average(test1, test2, test3, test4, test5)
    # The variable "grade_average" is assigned the return value from the function "determine_grade".
    # Calls the "determine_grade" function, passed with the argument "score_average".
    grade_average = determine_grade(score_average)
    # Prints the score and grade average, which "grade_average" and "score_average".
    print("Your have a(n) " + grade_average + " with an average test score of " + format(score_average, ',.1f') + "%.")


# Defines the function "calc_score_average" with the 5 parameters "t1-t5".
def calc_average(t1, t2, t3, t4, t5):
    # The variable average_score is assigned the value of the average of "t1-t5".
    average_score = (t1 + t2 + t3 + t4 + t5) / 5
    # Returns the variable "average_score" to the called function, which is assigned to the variable "grade_average".
    return average_score


# Defines the function "determine_grade" with the parameter "test".
def determine_grade(test):
    score = int(round(test))
    if score >= 90:
        return "A"
    elif 90 > score >= 80:
        return "B"
    elif 80 > score >= 70:
        return "C"
    elif 70 > score >= 60:
        return "D"
    else:
        return "F"
main()
