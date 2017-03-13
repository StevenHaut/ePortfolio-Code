# Defines the empty list "monthly_rainfall".
monthly_rainfall = []
# Defines the global variable "total_rainfall" with a value of 0.
total_rainfall = 0
# Defines the global variable "average_monthly_rainfall" with a value of 0.
average_monthly_rainfall = 0


# Defines the function "main".
def main():
    # Calls the "create_rainfall_list" function.
    create_rainfall_list()
    # Calls the "determine_max_rainfall" function.
    determine_max_rainfall()
    # Calls the "determine_min_rainfall" function.
    minimum = determine_min_rainfall()
    # Calls the "determine_max_rainfall" function.
    maximum = determine_max_rainfall()
    # Calls the "average_rainfall" function.
    average_rainfall()
    # Calls the "print_total" function, passed with the arguments "minimum" and "maximum".
    print_total(minimum, maximum)


# Defines the function "create_rainfall_list".
def create_rainfall_list():
    # Executes a try suite.
    try:
        # Executes twelve times starting with months = 1 and ending with months = 12.
        for months in range(1, 13):
            # The variable "month" is equal the called function "determine_month_name", pass with the argument "months".
            month = determine_month_name(months)
            # Adds user input to the "monthly_rainfall" list.
            monthly_rainfall.append(float(input("Enter the inches of rainfall in " + str(month) + ": ")))
    # The except clause specifies the ValueError exception.
    except ValueError:
        # Displays an error message on the screen.
        print("Entered value is invalid.")
        # The variable "want_continue" is defined as the user's input.
        # Asks the user to enter Y to continue.
        want_continue = input("Do you want to continue? Enter Y (for Yes).")
        # If the user enter 'Y', the function "create_rainfall_list" is recalled.
        if want_continue is 'Y':
            create_rainfall_list()
        # If the user enter 'y', the function "create_rainfall_list" is recalled.
        elif want_continue is 'y':
            create_rainfall_list()
        # If the user enters anything besides 'Y' or 'y', the program ends.
        else:
            quit()


# Defines the function "determine_max_rainfall".
def determine_max_rainfall():
    # The variable "maximum" equals the maximum value in the list "monthly_rainfall".
    maximum = max(monthly_rainfall)
    # Returns the variable "maximum".
    return maximum


# Defines the function "determine_min_rainfall".
def determine_min_rainfall():
    # The variable "minimum equals the minimum value in the list "monthly_rainfall".
    minimum = min(monthly_rainfall)
    # Returns the variable "minimum".
    return minimum


# Defines the function "average_rainfall".
def average_rainfall():
    # Calls the global variable "total_rainfall".
    global total_rainfall
    # Calls the global variable "average_monthly_rainfall".
    global average_monthly_rainfall
    # The variable "total_rainfall" equals the sum of the list "monthly_rainfall".
    total_rainfall = sum(monthly_rainfall)
    # The variable "average_monthly_rainfall" equals the total rainfall divided by 12 months.
    average_monthly_rainfall = total_rainfall/12


# Defines the function "determine_month_num" with parameter "month".
def determine_month_num(month):
    # Executes the number of times that is equal to the length of the list "monthly_rainfall".
    for months in range(len(monthly_rainfall)):
        # If the parameter "month" is equal to the value of the number equal to "months" in the list "monthly_rainfall",
        # then everything beneath executes.
        if month == monthly_rainfall[months]:
            # The variable "month" equals the place value, "months", in the list, plus one.
            month = months + 1
            # The variable "month" equals the called function "determine_month_name", passed with the argument "month".
            month = determine_month_name(month)
            # Returns the variable "month".
            return month
        # If the if statement isn't correct, the function continues.
        else:
            continue


# Defines the function "determine_month_name" with parameter "months".
def determine_month_name(months):
    # If the variable "months" equals the number "1", then the variable months equals "January".
    if months == 1:
        months = "January"
    # If the variable "months" equals the number "2", then the variable months equals "February".
    elif months == 2:
        months = "February"
    # If the variable "months" equals the number "3", then the variable months equals "March".
    elif months == 3:
        months = "March"
    # If the variable "months" equals the number "4", then the variable months equals "April".
    elif months == 4:
        months = "April"
    # If the variable "months" equals the number "5", then the variable months equals "May".
    elif months == 5:
        months = "May"
    # If the variable "months" equals the number "6", then the variable months equals "June".
    elif months == 6:
        months = "June"
    # If the variable "months" equals the number "7", then the variable months equals "July".
    elif months == 7:
        months = "July"
    # If the variable "months" equals the number "8", then the variable months equals "August".
    elif months == 8:
        months = "August"
    # If the variable "months" equals the number "9", then the variable months equals "September".
    elif months == 9:
        months = "September"
    # If the variable "months" equals the number "10", then the variable months equals "October".
    elif months == 10:
        months = "October"
    # If the variable "months" equals the number "11", then the variable months equals "November".
    elif months == 11:
        months = "November"
    # If the variable "months" equals the number "12", then the variable months equals "December".
    elif months == 12:
        months = "December"
    # Returns the variable "months".
    return months


# Defines the function "print_total" with parameters "minimum" and "maximum".
def print_total(minimum, maximum):
    # The variable "month_max" equals the called function "determine_month_num", passed with the argument "maximum".
    month_max = determine_month_num(maximum)
    # The variable "month_min" equals the called function "determine_month_num", passed with the argument "minimum".
    month_min = determine_month_num(minimum)
    # Displays the total rainfall, in inches to two decimal places, on the screen.
    print("The total amount of rainfall for the year is " + str(format(total_rainfall, ',.2f')) + " inches")
    # Displays the average monthly rainfall, in inches to two decimal places, on the screen.
    print("The average monthly rainfall is " + str(format(average_monthly_rainfall, ',.2f')) + " inches per month")
    # Displays the maximum amount of rainfall, in inches to two decimal places, on the screen.
    print("The maximum amount of rainfall was " + str(format(maximum, ',.2f')) + " inches in " + str(month_max))
    # Displays the minimum amount of rainfall, in inches to two decimal places, on the screen.
    print("The minimum amount of rainfall was " + str(format(minimum, ',.2f')) + " inches in " + str(month_min))
# Calls the "main" function.
main()
