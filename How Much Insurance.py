# Defines the function main.
def main():
    # Asks the user for the replacement cost of a building.
    # The variable "replacement_cost" is assigned the entered value.
    replacement_cost = float(input("Enter the replacement cost of a building: "))
    # Calls the calculate function and passes the argument "replacement_cost".
    calculate(replacement_cost)


# Defines the function calculate with the parameter "cost".
def calculate(cost):
    #  Calculates the amount to insure the building for by taking 80% of the cost.
    minimum_insurance_value = cost * 0.8
    # Displays the calculated value.
    print("The minimum amount of insurance needed for $" + format(cost, ',.2f') +
          " is $" + format(minimum_insurance_value, ',.2f') + ".")

# Calls the main function.
main()
