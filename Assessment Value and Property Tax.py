# Defines the function "main".
def main():
    # Asks the user for the actual value of a piece of property.
    # The variable "property_value" is assigned the entered value and then passed to the "calculate" function.
    property_value = float(input("Enter the actual value of a piece of property: "))
    # Calls the "calculate" function and passes the argument "property_value".
    calculate(property_value)


# Defines the function calculate with the parameter "value".
def calculate(value):
    # Calculates "assessment_value" based on the parameter "value", which is accepted as "property_value", multiplied by 60%.
    assessment_value = value * 0.6
    # Calculated "property_tax" based on the parameter "assessment_value" multiplied by 0.72 for every $100.00.
    property_tax = assessment_value * 0.0072
    # Prints the assessment value and property tax on the screen, using "assessment_value" and "property_tax".
    print("The assessment value is is $" + format(assessment_value, ',.2f') + " and the property tax is $" + format(property_tax, ',.2f') + ".")


# Calls the "main" function.
main()
