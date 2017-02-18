# Defines the function "main".
def main():
    # Asks the user for the replacement cost of a building.
    # The variable "replacement_cost" is assigned the entered value and then passed to the "calculate" function.
    replacement_cost = float(input("Enter the replacement cost of a building: "))
    # Calls the calculate function and passes the argument "replacement_cost".
    calculate(replacement_cost)


# Defines the function calculate with the parameter "cost", which is accepted as the parameter "replacement_cost".
def calculate(cost):
    # Calculates "minimum_insurance_value", the amount to insure the building, by multiplying "cost" by 80%.
    minimum_insurance_value = cost * 0.8
    # Displays the calculated value using "cost", which is accepted as "replacement_cost",
    # and "minimum_insurance_value".
    print("The minimum amount of insurance needed for $" + format(cost, ',.2f') +
          " is $" + format(minimum_insurance_value, ',.2f') + ".")

# Calls the "main" function.
main()
