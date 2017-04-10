# Imports the program 'Personal_Info_Class'.
import Personal_Info_Class


# Defines the "main" function.
def main():
    # Calls the "create_my_data" function.
    create_my_data()
    # Calls the "create_my_friend_data" function.
    create_my_friend_data()
    # Calls the "create_my_brother_data" function.
    create_my_brother_data()


# Defines the "create_my_data" function.
def create_my_data():
    # Defines my name, address, age, and phone number.
    name = "Steven"
    address = '15007 Harmony Rd Huntley, IL'
    age = '25'
    phone_number = '847-888-5555'

    # Creates an instance of the Personal_Info_Class, with empty values.
    my_data = Personal_Info_Class.PersonalData("", "", "", "")

    # Assigns the values to the object's attributes.
    my_data.set_name(name)
    my_data.set_address(address)
    my_data.set_age(age)
    my_data.set_phone_number(phone_number)

    # Displays a message with the information on the screen.
    print("-------------------------------------- \n"
          "Here is the my information: ")
    print("Name: " + my_data.get_name())
    print("Address: " + my_data.get_address())
    print("Age: " + my_data.get_age())
    print("Phone Number: " + my_data.get_phone_number())


# Defines the "create_my_friend_data" function.
def create_my_friend_data():
    # Defines my friend's name, address, age, and phone number.
    name = "Anthony"
    address = '991 Concord Ln Huntley, IL'
    age = '26'
    phone_number = '847-224-9336'

    # Creates an instance of the Personal_Info_Class, with empty values.
    my_data = Personal_Info_Class.PersonalData("", "", "", "")

    # Assigns the values to the object's attributes.
    my_data.set_name(name)
    my_data.set_address(address)
    my_data.set_age(age)
    my_data.set_phone_number(phone_number)

    # Displays a message with the information on the screen.
    print("-------------------------------------- \n"
          "Here is the my friend's information: ")
    print("Name: " + my_data.get_name())
    print("Address: " + my_data.get_address())
    print("Age: " + my_data.get_age())
    print("Phone Number: " + my_data.get_phone_number())


# Defines the "create_my_brother_data" function.
def create_my_brother_data():
    # Defines my brother's name, address, age, and phone number.
    name = "Jason"
    address = '12344 Central Av. Hemet, CA'
    age = '29'
    phone_number = '224-586-6542'

    # Creates an instance of the Personal_Info_Class, with empty values.
    my_data = Personal_Info_Class.PersonalData("", "", "", "")

    # Assigns the values to the object's attributes.
    my_data.set_name(name)
    my_data.set_address(address)
    my_data.set_age(age)
    my_data.set_phone_number(phone_number)

    # Displays a message with the information on the screen.
    print("-------------------------------------- \n"
          "Here is the my brother's information: ")
    print("Name: " + my_data.get_name())
    print("Address: " + my_data.get_address())
    print("Age: " + my_data.get_age())
    print("Phone Number: " + my_data.get_phone_number())
# Calls the "main" function.
main()
