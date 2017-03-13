# Defines the function "main".
def main():
    # Calls the function "user_input_names".
    user_input_names()


# Defines the function "user_input_names".
def user_input_names():
    add_user_boy_name = input("Do you want to check a boys name? Enter Y (for Yes) or N (for No): ")
    if add_user_boy_name is 'Y':
        user_boy_name = input("Enter a boys name to be checked: ").title()
        check_boys_name(user_boy_name)
    elif add_user_boy_name is 'y':
        user_boy_name = input("Enter a boys name to be checked: ").title()
        check_boys_name(user_boy_name)
    add_user_girl_name = input("Do you want to check a girls name? Enter Y (for Yes) or N (for No): ")
    if add_user_girl_name is 'Y':
        user_girl_name = input("Enter a girls name to be checked: ").title()
        check_girls_name(user_girl_name)
    elif add_user_girl_name is 'y':
        user_girl_name = input("Enter a girls name to be checked: ").title()
        check_girls_name(user_girl_name)


# Defines the function "check_boys_name".
def check_boys_name(user_name):
    # Defines the variable "k" with a value of 0.
    k = 0
    # Executes a try suite.
    try:
        # Opening the file "BoyNames.txt" and associating it with the variable "boy_names_list".
        boy_names_list = open("BoyNames.txt", "r")
        # The variable "boy_names" equals the list of the lines in the associated file, breaking at line boundaries.
        boy_names = boy_names_list.read().splitlines()
        # Closes the file associated with the variable "boy_names_list".
        boy_names_list.close()
        # Executes the number of times that is equal to the length of the list "boy_names".
        for name in boy_names:
            # If the parameter "user_name" is the same "name" in the list "boy_names", then everything beneath executes.
            if name == user_name:
                # The variable "k" equals it's value plus one.
                k += 1
                # Displays the message that the entered name is a popular name.
                print("The name " + str(user_name) + " is a popular boy name.")
            # If the if statement isn't correct, the function continues.
            else:
                continue
        # If the value of the variable "k" is zero, a message is displayed that the entered name is not in the list.
        if k == 0:
            print(str(user_name) + " is not in the list.")
    # The except clause specifies the IOError exception.
    except IOError:
        # Displays an error message on the screen.
        print('An error occurred trying to read the file.')
        # Exits the program to avoid further errors.
        exit()


# Defines the function "check_girls_name".
def check_girls_name(user_name):
    # Defines the variable "k" with a value of 0.
    k = 0
    # Executes a try suite.
    try:
        # Opening the file "GirlNames.txt" and associating it with the variable "girl_names_list".
        girl_names_list = open("GirlNames.txt", "r")
        # The variable "girl_names" equals the list of the lines in the associated file, breaking at line boundaries.
        girl_names = girl_names_list.read().splitlines()
        # Closes the file associated with the variable "girl_names_list".
        girl_names_list.close()
        # Executes the number of times that is equal to the length of the list "girl_names".
        for name in girl_names:
            # If the parameter "user_name" is the same "name" in the list "girl_names", then everything beneath executes.
            if name == user_name:
                # The variable "k" equals it's value plus one.
                k += 1
                # Displays the message that the entered name is a popular name.
                print("The name " + str(user_name) + " is a popular girl name.")
            # If the if statement isn't correct, the function continues.
            else:
                continue
        # If the value of the variable "k" is zero, a message is displayed that the entered name is not in the list.
        if k == 0:
            print(str(user_name) + " is not in the list.")
    # The except clause specifies the IOError exception.
    except IOError:
        # Displays an error message on the screen.
        print('An error occurred trying to read the file.')
        # Exits the program to avoid further errors.
        exit()
# Calls the "main" function.
main()
