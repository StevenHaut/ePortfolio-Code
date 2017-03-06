# Defines the global variable "count" with a value of 0.
count = 0
# Defines the global variable "total" with a value of 0.
total = 0
# Defines the global variable "average" with a value of 0.
average = 0


# Defines the function "main".
def main():
    # Calls the "add_numbers" function.
    add_numbers()
    # Calls the "determine_average" function.
    determine_average()
    # Calls the global variable "average".
    global average
    # Calls the "print_average" function, passed with the argument "average".
    print_average(average)


# Defines the function "add_numbers".
def add_numbers():
    # Calls the global variable "total".
    global total
    # Executes a try suite.
    try:
        # Opening the file "numbers.txt" and associating it with the variable "read_number_list".
        read_number_list = open("numbers.txt", "r")
        # Reads the file's contents.
        for line in read_number_list:
            # Executes a try suite.
            try:
                # Adds the value of each consecutive line to value of the variable "total".
                total += int(line)
                # Calls the "number_counter" function.
                number_counter()
            # The except clause specifies the ValueError exception.
            except ValueError:
                print('Could not convert data to an integer.')
    # The except clause specifies the IOError exception.
    except IOError:
        print('An error occurred trying to read the file.')
        # Exits the program to avoid further errors.
        exit()


# Defines the function "number_counter".
def number_counter():
    # Calls the global variable "count".
    global count
    # Adds 1 to the value of the variable "count".
    count += 1


# Defines the function "determine_average".
def determine_average():
    # Calls the global variable "count".
    global count
    # Calls the global variable "total".
    global total
    # Calls the global variable "average".
    global average
    # Calculates the average value by dividing "total" by "count".
    average = total/count


# Defines the function "print_average" with parameter "number".
def print_average(number):
    # Calls the global variable "total".
    global total
    # Displays the total sum of numbers and their average to one decimal place.
    print("The total amount of " + str(total) + " averages to " + format(number, ',.1f') + ".")
# Calls the "main" function.
main()
