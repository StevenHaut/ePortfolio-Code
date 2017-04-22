# Defines the function 'main'
def main():

    # Defines the variables as user input
    number = int(input("Enter the number that you want to be raised to a power: "))
    power = int(input("Enter the power that you want " + str(number) + " to be raised to : "))

    # prints the called function, 'number_to_power', passed with the arguments 'number' and 'power'
    print(number_to_power(number, power))


# Defines the function 'number_to_power' with the parameters 'base' and 'exponent'
def number_to_power(base, exponent):
    # If the exponent is 0, it returns 1
    if exponent == 0:
        return 1
    # Otherwise, the below command executes.
    else:
        # Returns the base number times the recursive function  passed with the number and the value of the exponent reduced by 1.
        return base*number_to_power(base, exponent-1)
# Calls the 'main' function
main()
