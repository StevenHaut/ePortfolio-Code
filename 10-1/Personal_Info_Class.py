# Defines the 'PersonalData' Class.
class PersonalData:
    # The __init__ method initializes the attributes.
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # The set_name method sets the person's name.
    def set_name(self, name):
        self.__name = name

    # The set_address method sets the person's address.
    def set_address(self, address):
        self.__address = address

    # The set_age method sets the person's age.
    def set_age(self, age):
        self.__age = age

    # The set_phone_number method sets the person's phone number.
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # The get_name method returns the person's name.
    def get_name(self):
        return self.__name

    # The get_address method returns the person's address.
    def get_address(self):
        return self.__address

    # The get_age method returns the person's age.
    def get_age(self):
        return self.__age

    # The get_phone_number method returns the person's phone number.
    def get_phone_number(self):
        return self.__phone_number
