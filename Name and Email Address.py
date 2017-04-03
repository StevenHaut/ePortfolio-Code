# Defines the global variable 'names_and_emails' as a blank dictionary.
names_and_emails = {}


# Defines the function "main".
def main():
    # Calls the function "pickle_dictionary".
    pickle_dictionary()
    # Calls the function "user_input_names".
    display_menu()
    # Calls the function " display_menu".


# Defines the function "pickle_dictionary".
def pickle_dictionary():
    # Calls the global variable 'names_and_emails'.
    global names_and_emails
    # Imports the pickle module.
    import pickle
    # Executes a try suite.
    try:
        # Opens the file 'name&emails.dat' for binary reading.
        input_file = open('name&emails.dat', 'rb')
        # Calls the pickle module's load function to retrieve and unpickle an object from the file 'name&emails.dat'.
        # The object is then assigned to the variable 'names_and_emails'.
        names_and_emails = pickle.load(input_file)
        # Closes the file 'name&emails.dat'.
        input_file.close()
    # The except clause specifies the IOError exception.
    except IOError:
        # Displays an error message on the screen.
        print('There are currently no records. An empty dictionary has been created.')


# Defines the function "save_and_close_pickle".
def save_and_close_pickle():
    # Calls the global variable 'names_and_emails'.
    global names_and_emails
    # Imports the pickle module.
    import pickle
    # Opens the file 'name&emails.dat' for binary writing.
    output_file = open('name&emails.dat', 'wb')
    # Calls pickle module's dump function to serialize the dictionary,
    # 'name_and_emails', and write it to the 'name&emails.dat' file.
    pickle.dump(names_and_emails, output_file)
    # Closes the 'name&emails.dat' file.
    output_file.close()


# Defines the function "display_menu".
def display_menu():
    # Displays a Menu and defines the variable 'user_input' as the user's entry.
    user_input = input("                      Main Menu \n"
                       "-------------------------------------------------------- \n"
                       "'look up': to look up a person's email address. \n"
                       "'add': to add a new name and email address. \n"
                       "'change': to change an existing email address. \n"
                       "'delete': to delete an existing name and email address. \n"
                       "'quit': to save the dictionary and end the program. \n"
                       "-------------------------------------------------------- \n"
                       "Enter 'look up', 'add', 'change', 'delete', or 'quit': ").title()
    print('--------------------------------------------------------')
    # Calls the function 'initiate_function', passed with the variable 'user_input'.
    initiate_function(user_input)


# Defines the function "initiate_function", with the parameter 'user_input'.
def initiate_function(user_input):
    # If the user entered 'look up', the function 'look_up_email' is called.
    if user_input.upper() == "LOOK UP":
        look_up_email()
    # If the user entered 'add', the function 'add_new_email' is called.
    elif user_input.upper() == "ADD":
        add_new_email()
    # If the user entered 'change', the function 'change_email' is called.
    elif user_input.upper() == "CHANGE":
        change_email()
    # If the user entered 'delete', the function 'delete_email' is called.
    elif user_input.upper() == "DELETE":
        delete_email()
    # If the user entered 'quit', the functions 'save_and_close_pickle' and 'quit' are called.
    elif user_input.upper() == "QUIT":
        save_and_close_pickle()
        quit()


# Defines the function "look_up_email".
def look_up_email():
    # The variable 'name' is defined as the user's entry.
    name = input("Enter a person's name to look up their email: ").title()
    print('--------------------------------------------------------')
    # If the name associated with 'name' is in 'names_and_emails', then the below command executes.
    if name in names_and_emails:
        # Displays a message with the email on the screen.
        print(name + "'s email is " + names_and_emails[name] + "\n"
              "-------------------------------------------------------- \n")
    # If the if statement isn't correct, a message displays.
    else:
        print(name + ' is not an existing name in the dictionary. \n'
                     '-------------------------------------------------------- ')
    # Calls the 'display_menu' function.
    display_menu()


# Defines the function "add_new_email".
def add_new_email():
    # The variable 'name' is defined as the user's entry.
    name = input("Enter the name of the person you wish to add: ").title()
    # If the name associated with 'name' is NOT in 'names_and_emails', then the below command executes.
    if name not in names_and_emails:
        # The variable email equals the user's entry.
        email = input('Enter the email for ' + name + ': ')
        # Changes the value for the key, 'name', to the variable 'email'
        names_and_emails[name] = email
        # Displays a confirmation message with the email on the screen.
        print(name + "'s email " + names_and_emails[name] + " was added. \n"
              "-------------------------------------------------------- \n")
    # If the if statement isn't correct, a message displays.
    else:
        print(name + ' was already added to the dictionary. \n'
                     '-------------------------------------------------------- ')
    # Calls the 'display_menu' function.
    display_menu()


# Defines the function "change_email".
def change_email():
    # The variable 'name' is defined as the user's entry.
    name = input("Enter the name of the person who's email you wish to change: ").title()
    # If the name associated with 'name' is in 'names_and_emails', then the below command executes.
    print('--------------------------------------------------------')
    if name in names_and_emails:
        # The variable 'new_email' equals the user's entry.
        new_email = input('Enter the new email for ' + name.title() + ': ')
        # The variable 'user_answer" equals the user's entry.
        user_answer = input("Are you sure you want to change " + name + "'s email to " + new_email + "? \n"
                            "-------------------------------------------------------- \n"
                            "Enter 'Y'(for Yes) or 'N'(for No): ")
        print('--------------------------------------------------------')
        # If the user enter's 'Y', then the new name and email is added to the dictionary.
        if user_answer.upper() == 'Y':
            names_and_emails[name] = new_email
        # If the if statement isn't correct, a message displays.
        else:
            # Displays a message that there were no changes.
            print('No changes have been made. /n '
                  '--------------------------------------------------------')
            # Calls the " display_menu" function.
            display_menu()
    # If the if statement isn't correct, a message displays.
    else:
        print(name + ' is not an existing name in the dictionary. \n'
                     '-------------------------------------------------------- ')
    # Calls the 'display_menu' function.
    display_menu()


# Defines the function "delete_email".
def delete_email():
    # The variable 'name' is defined as the user's entry.
    name = input("Enter the name of the person you wish to delete: ").title()
    # If the name associated with 'name' is in 'names_and_emails', then the below command executes.
    if name in names_and_emails:
        # The variable 'user_answer" equals the user's entry.
        user_answer = input("Are you sure you want to delete " + name + "'s email? \n"
                            "-------------------------------------------------------- \n"
                            "Enter 'Y'(for Yes) or 'N'(for No): ")
        print('--------------------------------------------------------')
        # If the user enter's 'Y', then the name and email are deleted from the dictionary.
        if user_answer.upper() == 'Y':
            del names_and_emails[name]
        # If the if statement isn't correct, a message displays.
        else:
            # Calls the " display_menu" function.
            display_menu()
    # If the if statement isn't correct, a message displays.
    else:
        print(name + ' is not an existing name in the dictionary. \n'
                     '-------------------------------------------------------- ')
    # Calls the " display_menu" function.
    display_menu()
# Calls the "main" function.
main()
