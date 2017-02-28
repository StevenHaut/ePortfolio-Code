# Calls the function "random" stored in random module.
import random
# The variable "num1" is assigned the randomly generated number between 0 and 1000.
num1 = random.randrange(1000)
# The variable "num2" is assigned the randomly generated number between 0 and 1000.
num2 = random.randrange(1000)
# The variable "quiz_sum" is assigned the calculated sum of "num1" and "num2".
quiz_sum = num1 + num2


# Defines the function "main".
def main():
    # Asks the user for the sum of "num1" and "num2".
    # The variable "user_answer" is assigned the entered value and then passed to the "determine answer" function.
    user_answer = int(input("What is the sum of " + str(num1) + " and " + str(num2) + ": "))
    # Calls the "determine_answer" function, passed with the argument "user_answer".
    determine_answer(user_answer)


# Defines the function "determine_answer".
def determine_answer(answer):
    # If the parameter "answer", associated with "user_answer", equals the variable
    # "quiz_sum", the program continues to the print command under "if".
    if answer == quiz_sum:
        # Prints a congratulations message on the screen.
        print("Congratulations!!! That is the correct answer.")
    # If the parameter "answer" does not equal the variable "quiz_sum",
    # the program continues to the print command under "else".
    else:
        # Prints a sorry message on the screen that displays the corrected answer, using the variable "quiz_sum".
        print("Sorry, " + str(quiz_sum) + " is the correct answer.")
# Calls the "main" function.
main()
