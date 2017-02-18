# Defines the function "main".
def main():
    # Asks the user to enter the monthly cost for the subsequent expenses.
    print("Enter the monthly costs for the following expenses incurred from operating your automobile:")
    # The variable "loan_payment" is assigned the entered value.
    loan_payment = float(input("Loan payment: "))
    # The variable "insurance" is assigned the entered value.
    insurance = float(input("Insurance: "))
    # The variable "gas" is assigned the entered value.
    gas = float(input("Gas: "))
    # The variable "oil" is assigned the entered value.
    oil = float(input("Oil: "))
    # The variable "tires" is assigned the entered value.
    tires = float(input("Tires: "))
    # The variable "maintenance" is assigned the entered value.
    maintenance = float(input("Maintenance: "))
    # Accumulates the total monthly cost as a local variable, "total_monthly_cost".
    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    # Prints the total monthly costs on the screen, using "total_monthly_cost".
    print("The total monthly cost of your automobile expenses is $" + format(total_monthly_cost, ',.2f') + ".")
    # Calls the "calculate" function and passes the argument "total_monthly_cost".
    calculate(total_monthly_cost)


# Defines the function calculate with the parameter "cost".
def calculate(cost):
    # Calculates "total_annual_cost" based on the parameter cost which is accepted as "total_monthly_cost".
    total_annual_cost = cost * 12
    # Prints the total annual costs on the screen, using "total_annual_cost".
    print("The total annual cost of your automobile expenses is $" + format(total_annual_cost, ',.2f') + ".")

# Calls the "main" function.
main()
