import Personal_Info_Class


def main():
    create_my_data()
    create_my_friend_data()
    create_my_brother_data()


def create_my_data():
    name = "Steven"
    address = '15007 Harmony Rd Huntley, IL'
    age = '25'
    phone_number = '8478885555'

    my_data = Personal_Info_Class.PersonalData(name, address, age, phone_number)
    print("-------------------------------------- \n"
          "Here is the my information: ")
    print("Name: " + my_data.get_name())
    print("Address: " + my_data.get_address())
    print("Age: " + my_data.get_age())
    print("Phone Number: " + my_data.get_phone_number())


def create_my_friend_data():
    name = "Anthony"
    address = '991 Concord Ln Huntley, IL'
    age = '26'
    phone_number = '8472249336'

    my_friend_data = Personal_Info_Class.PersonalData(name, address, age, phone_number)
    print("-------------------------------------- \n"
          "Here is the my friend's information: ")
    print("Name: " + my_friend_data.get_name())
    print("Address: " + my_friend_data.get_address())
    print("Age: " + my_friend_data.get_age())
    print("Phone Number: " + my_friend_data.get_phone_number())


def create_my_brother_data():
    name = "Jason"
    address = '12344 Central Av. Hemet, CA'
    age = '29'
    phone_number = '2245866542'

    my_brother_data = Personal_Info_Class.PersonalData(name, address, age, phone_number)
    print("-------------------------------------- \n"
          "Here is the my brother's information: ")
    print("Name: " + my_brother_data.get_name())
    print("Address: " + my_brother_data.get_address())
    print("Age: " + my_brother_data.get_age())
    print("Phone Number: " + my_brother_data.get_phone_number())
main()
