# Defines the function "main".
def main():
    # The variable "full_name" equals the called function "get_string".
    full_name = get_string()
    # The variable "stripped_initials" equals the called function "strip_initials", passed with the argument "full_name".
    stripped_initials = strip_initials(full_name)
    # Calls the function "print_initials", passed with the argument "stripped_initials".
    print_initials(stripped_initials)


# Defines the function "get_string".
def get_string():
    # The variable "string" equals the entered string.
    string = input("Enter your first, middle, and last names: ")
    # Returns the string "string".
    return string


# Defines the function "strip_initials" with the parameter "name_string".
def strip_initials(name_string):
    # Splits the string "name_string".
    name_string = name_string.split()
    # Defines the variable "initials".
    initials = ''
    # Executes the below commands for each "name" in the string "name_string".
    for name in name_string:
        # The variable "initials" adds the uppercase of the first letter in each "name"
        initials += (name[0].upper() + '.')
    # Returns the variable "initials".
    return initials


# Defines the function "print_initials" with the parameter "initials".
def print_initials(initials):
    # Displays a message with the user's initials.
    print(initials)
# Calls the "main" function.
main()
