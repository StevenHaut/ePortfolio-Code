# Defines the empty list "numbers_list".
numbers_list = []
# Defines the global variable "user_number" with a value of 0.
user_number = 0


# Defines the function "main".
def main():
    # Calls the global variable "user_number".
    global user_number
    # Calls the "random_numbers_list" function.
    random_numbers_list()
    # Calls the "get_user_number" function.
    user_number = get_user_number()
    # The variable "larger_numbers_list" equals the called function "check_numbers_against_list", passed with the
    # arguments "user_number" and ""
    larger_numbers_list = check_number_against_list(user_number, numbers_list)
    print_list(larger_numbers_list)


# Defines the function "random_numbers_list".
def random_numbers_list():
    # Calls the function "random" stored in random module.
    import random
    # The variable "num1" is assigned the randomly generated number between 0 and 1000.
    for number in range(0, 20):
        numbers_list.append(int(random.randrange(100)))


# Defines the function "get_user_number".
def get_user_number():
    # Executes a try suite.
    try:
        # The variable "user_num" equals the entered integer value.
        user_num = int(input("Enter an integer between 1 and 100: "))
        # If the variable "user_num" is between 1 and 100, the variable is returned.
        if 0 < user_num <= 100:
            return user_num
        # If the variable "user_num" is not between 1 and 100, an error message is displayed and the function restarts.
        elif 0 > user_num or user_num > 100:
            print("Invalid input. Number must be between 1 and 100.")
            get_user_number()
        # If the variable "user_num" is not an integer, an error message is displayed and the function restarts.
        else:
            print("Invalid input. You must enter an integer between 1 and 100.")
            get_user_number()
    # The except clause specifies the ValueError exception.
    except ValueError:
        # An error message is displayed on the screen.
        print("Input value has resulted in an error.")
        # The variable "want_continue" is equal to the user input.
        want_continue = input("Do you want to continue? Enter Y (for Yes): ")
        # If the variable "want_continue" is equal to Y, the function restarts.
        if want_continue is 'Y':
            get_user_number()
        # If the variable "want_continue" is equal to y, the function restarts.
        elif want_continue is 'y':
            get_user_number()
        # If the variable "want_continue" is not equal to Y or y, the program ends.
        else:
            quit()


# Defines the function "check_number_against_list", with the parameters "user_num" and "num_list".
def check_number_against_list(user_num, num_list):
    # Defines the empty list "larger_num_list".
    larger_num_list = []
    # Executes the number of times that is equal to the length of the list "num_list".
    for num in range(len(num_list)):
        # If the parameter "user_num" is less than the value of the number equal to "num" in the list "numbers_list",
        # then everything beneath executes.
        if user_num < numbers_list[num]:
            # The value of the number equal to "num" in the list "numbers_list" is added to the list "larger_num_list".
            larger_num_list.append(numbers_list[num])
        # If the if statement isn't correct, the function continues.
        else:
            continue
    # Returns the list "larger_num_list".
    return larger_num_list


# Defines the function "print_list", passed with the parameter "num_list".
def print_list(num_list):
    # If the list "num_list" is empty, it displays a message saying there there are no greater numbers.
    if not num_list:
        print("There are no numbers in the list greater than the entered number.")
    # If the list "num_list" is not empty, it displays the numbers that are greater than the entered number.
    else:
        print("The numbers greater than the entered number are: " + str(num_list))
# Calls the function "main".
main()
