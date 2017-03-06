# Defines the global variable "count" with a value of 0.
count = 0


# Defines the function "main".
def main():
    # Calls the "read_list" function.
    read_list()
    # Calls the global variable "count".
    global count
    # Calls the "print_count" function, passed with the argument "count".
    print_count(count)


# Defines the function "read_list".
def read_list():
    # Opening the file "names.txt" and associating it with the variable "read_names".
    read_names = open("names.txt", "r")
    # Reads the file's contents.
    for line in read_names:
        # Displays the files contents on the screen, using "line" for each line.
        print(line)
        # Calls the "name_counter" function.
        name_counter()


# Defines the function "name_counter".
def name_counter():
    # Calls the global variable "count".
    global count
    # Adds 1 to the value of the variable "count".
    count += 1


# Defines the function "print_count" with parameter "number".
def print_count(number):
    # Displays the calculated number of names on the screen, using "number".
    print("The number of names read from the file is " + str(number))
# Calls the "main" function.
main()
