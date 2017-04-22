# Defines the function 'main'
def main():
    # The variable 'num_list' equals the called function 'get_list'
    num_list = get_list()
    # Prints the called function 'calc_sum' passed with the argument 'num_list'
    print(calc_sum(num_list))


# Defines the function 'get_list'
def get_list():
    # The variable 'num_list' equals the entered list
    num_list = input('Enter a list of numbers, separated by commas: ').split(',')
    # Returns the 'num_list'
    return num_list


# Defines the function 'calc_sum' with the parameter 'num'
def calc_sum(num):
    # If the length of the list is 1, the number is returned
    if len(num) == 1:
        return int(num[0])
    # Otherwise the below command executes.
    else:
        # Returns the integer value of the first number in the list added to the integer value of recursive function passed with the rest of the list as the argument.
        return int(num[0]) + int(calc_sum(num[1:]))
# Calls the 'main' function
main()
