# Defines the 'Employee' Parent Class holds general information about office furniture.


class Employee(object):
    """
        The __init__ method accepts name, number
    """
    def __init__(self, name, number):

        # Initializes the attributes

        self.__name = name
        self.__number = number

    # Adds the mutator methods to change the object's value.

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # Adds accessor methods to return information

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Defines the __str__ method and returns the string 'info_string'
    def __str__(self):
        info_string = '----------------------------------------------------------------------------------------' + '\nEmployee name: ' + self.__name + '  Employee Number: ' + str(self.get_number()) + '\n----------------------------------------------------------------------------------------'
        return info_string


# Defines the  subclass 'ProductionWorker' of the 'Employee' class.
class ProductionWorker(Employee):
    """
        The __init__ method accepts arguments for name, number
    """
    def __init__(self, name, number, shift_num, hourly_rate):
        # Calls the parent class 'Employee' and passes arguments to it.
        Employee.__init__(self, name, number)

        # Initializes the shift_num and hourly_rate

        self.__shift_num = shift_num
        self.__hourly_rate = hourly_rate

    # Adds the mutator methods to change the object's value

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    # Adds accessor methods to return information

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_rate(self):
        return self.__hourly_rate

    # Overwrites the __str__ method and returns the string 'info_string'
    def __str__(self):
        info_string = '----------------------------------------------------------------------------------------' + '\nEmployee name: ' + self.get_name() + '  Employee Number: ' + str(self.get_number()) + '  Shift Number: ' + str(self.__shift_num) + "  Hourly Pay Rate: ${:0,.2f}".format(self.__hourly_rate) + '\n----------------------------------------------------------------------------------------'
        return info_string
