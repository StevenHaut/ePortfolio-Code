# Defines the function 'main'
def main():
    # The variable 'num' equals the called function 'get_integer'
    num = get_integer()
    # Calls the function 'print_integer', passed with the argument 'num'
    print_integer(num)


# Defines the function 'get_integer'
def get_integer():
    # The variable 'num' equals the integer value of the entered number
    num = int(input('Enter an integer for the count up to stop at: '))
    # Returns the variable 'num'
    return num


# Defines the function 'print_integer', with the parameter 'num'
def print_integer(num):
    # If the value of 'num' is greater than or equal to one, then everything below executes
    if num >= 1:
        # Calls the function ' print_integer', passed with the argument 'num - 1', which initiates the recursion, then prints the variable 'num'
        print_integer(num - 1), print(num)
# Calls the 'main' function
main()
