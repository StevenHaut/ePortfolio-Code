# Defines the function "main".
def main():
    # The variable "alpha_numeric_phone_number" equals the called function "get_string".
    alpha_numeric_phone_number = get_string()
    # The variable "translated_num" equals the called function "translate_number",
    # passed with the argument "alpha_numeric_phone_number".
    translated_num = translate_number(alpha_numeric_phone_number)
    # Call the function "print_phone_number" passed with the argument "translated_num".
    print_phone_number(translated_num)


# Defines the function "get_string".
def get_string():
    # The variable "string" equals the entered string.
    string = input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")
    # Returns the string "string".
    return string


# Defines the function "translate_number" with the parameter "alpha_num_string".
def translate_number(alpha_num_string):
    # The variable "new_phone_num" is equal to the string "alpha_num_string".
    new_phone_num = alpha_num_string
    # Executes the below commands for each "alpha_num" in the string "alpha_num_string".
    for alpha_num in alpha_num_string:
        # The variable "num" equals the called function "get_name", passed with the argument "alpha_num".
        num = get_num(alpha_num)
        # The string "new_phone_name" is replaced with the "num" in place of "alpha_num".
        new_phone_num = str.replace(new_phone_num, alpha_num, str(num))
    # Returns the string "new_phone_num".
    return new_phone_num


# Defines the function "get_num" with the parameter "alpha".
def get_num(alpha):
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    if alpha.upper() in ['A', 'B', 'C']:
        # Returns the number.
        return 2
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['D', 'E', 'F']:
        # Returns the number.
        return 3
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['G', 'H', 'I']:
        # Returns the number.
        return 4
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['J', 'K', 'L']:
        # Returns the number.
        return 5
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['M', 'N', 'O']:
        # Returns the number.
        return 6
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['P', 'Q', 'R', 'S']:
        # Returns the number.
        return 7
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['T', 'U', 'V']:
        # Returns the number.
        return 8
    # If the uppercase parameter "alpha" is in the list, the command below executes.
    elif alpha.upper() in ['W', 'X', 'Y', 'Z']:
        # Returns the number.
        return 9
    # If the parameter "alpha" not a letter, the command below executes.
    else:
        # Returns the variable "alpha".
        return alpha


# Defines the function "print_initials" with the parameter "initials".
def print_phone_number(number):
    # Displays a message with the phone number.
    print(number)
# Calls the "main" function.
main()
