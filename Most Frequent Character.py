# Defines the function "main".
def main():
    # Defines the variable "user_string" as equal to the return of the called function "get_string".
    entered_string = get_string()
    # Defines the variable "most_used_letter" equal to the called function "determine_most_used",
    # passed with the argument "entered_string".
    most_used_letter = determine_most_used(entered_string)
    # Calls the function "print_results", passed with the argument "most_used_letter".
    print_results(most_used_letter)


# Defines the function "get_string".
def get_string():
    # Defines the variable "start" as equal to 1.
    start = 1
    # While the variable "start" equals 1, the below commands execute.
    while start == 1:
        # The variable "string" equals the entered string.
        string = input("Enter a string to find out which letter is used the most: ")
        # If the string "string" is blank or only contains spaces, the below commands execute.
        if string is '' or ' ':
            # Displays a message on the screen that states the string is empty.
            print("You entered an empty string.")
            # The variable "want_continue" equals the entered character. Asks the user to enter 'Y' to continue.
            want_continue = input("If you want to continue, enter Y (for yes): ")
            # If the uppercase variable "want_continue" is Y, the below command executes.
            if want_continue.upper() == 'Y':
                # The variable "start" is set equal to 1, causing the while command to restart.
                start = 1
            # If the variable "want_continue" is not equal to Y or y, the program ends.
            else:
                # Displays a message that the program has ended.
                print("Program has ended.")
                # Ends the program.
                quit()
        else:
            start += 1
            # Returns the string "string".
            return string


# Defines the function "determine_most_used" with the parameter "string".a
def determine_most_used(user_string):
    # Defines the variable "maximum" as equal to zero.
    maximum = 0
    # Defines the variable "most_used".
    most_used = ''
    # Executes the below commands for each character, "letter1", in the string "user_string".
    for letter1 in user_string:
        # Defines the variable "count" as equal to zero.
        count = 0
        # Executes the below commands for each character, "letter2", in the string "user_string".
        for letter2 in user_string:
            # If lowercase parameter "letter1" is the same as lowercase parameter "letter2", below commands execute.
            if letter1.lower() == letter2.lower():
                # The "count" variable increase it's numeric value by 1.
                count += 1
            # If the 'if command' is False the below command executes.
            else:
                # The program continues.
                continue
            # If the value of "maximum" is less than the value of "count", the below commands execute.
            if maximum < count:
                # The variable "maximum" equals the value of the variable "count".
                maximum = count
                # The variable "most_used" equals the lowercase character of parameter "letter1".
                most_used = letter1.lower()
            # If the value of "maximum" equals the value of "count", the below commands execute.
            elif maximum == count:
                # If character, "letter1", is not in the string, "most_used", the below command executes.
                if letter1 not in most_used:
                    # The variable "most_used" adds a comma, space, and the lowercase character "letter1".
                    most_used += (', ' + letter1.lower())
                # If the 'if command' is False the below command executes.
                else:
                    # The program continues.
                    continue
    # Returns the variable "most_used"
    return most_used


# Defines the function "print_results" with the parameter "results".
def print_results(results):
    # If the length of "results" is longer than 1 character, the below commands execute.
    if len(results) > 1:
        # The string "results" adds "and " to the string before the last character.
        results = results[0:-1] + "and " + results[-1:]
        # Displays a message with the results on the screen.
        print('The characters that appears most frequently are "' + str(results) + '".')
    else:
        # Displays a message with the results on the screen.
        print('The character that appears most frequently is "' + results + '".')
# Calls the "main" function.
main()
