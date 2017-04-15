# Imports the program "employee".
import employee


# Defines the function 'main'.
def main():
    # Defines the variables as zero.
    shift = 0
    number = 0
    pay_rate = 0

    # Defines the variables as the user's input
    print("Enter the following information: " + '\n----------------------------------')
    name = input("Employee name: ")

    # While the variable 'number' equals zero, everything below executes
    while number == 0:
        try:
            # The variable 'number' equals the entered value.
            number = int(input("Employee number: "))
        # The except clause specifies the ValueError exception.
        except ValueError:
            print('The answer must be a number. Try Again. \n')

    # while the variable shift is not 1 or 2, everything below executes
    while shift not in [1, 2]:
        # Executes a try suite.
        try:
            # The variable 'shift' equals the entered value.
            shift = int(input("Shift Number [Day = 1, Night = 2]: "))
            # If the entered value is not 1 or 2, a message is displayed on the screen.
            if shift not in [1, 2]:
                print("The answer must be either 1 or 2. Try Again. \n")
        # The except clause specifies the ValueError exception.
        except ValueError:
            print('The answer must be a number. Try Again. \n')

    # While the variable 'pay_rate' equals zero, everything below executes
    while pay_rate == 0:
        # Executes a try suite.
        try:
            # The variable 'pay_rate' equals the entered value.
            pay_rate = float(input("Hourly Pay Rate: "))
        # The except clause specifies the ValueError exception.
        except ValueError:
            print('The answer must be a number. Try Again. \n')

    # Creating an object of the OfficeFurniture class.
    worker = employee.ProductionWorker(name, number, shift, pay_rate)

    # Displays the returned string containing the information
    print(worker)

    # Displays the information
    print('Employee Name: ' + worker.get_name())
    print('Employee Number: ' + str(worker.get_number()))
    shifts = worker.get_shift_num()
    if shifts == 1:
        shifts = 'Day'
    else:
        shifts = 'Night'
    print('Shift: ' + shifts)
    print('Hourly Rate: ' + "${:0,.2f}".format(worker.get_hourly_rate()))
# Calls the 'main' function
main()
