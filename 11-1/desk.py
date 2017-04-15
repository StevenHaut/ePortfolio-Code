# Imports the program "officeFurniture".
import officeFurniture


# Defines the function 'main'.
def main():
    # Creating an object of the OfficeFurniture class.
    desk = officeFurniture.Desk('Double-Pedestal Desk', 'Cherry Wood', 30, 65, 30, 350.00, 'Both', 9)

    # Displays the returned string containing the information
    print(desk)

    # Displays the information
    print('Furniture: ' + desk.get_category())
    print('Material: ' + desk.get_material())
    print('Dimensions(L x W x H): ' + str(desk.get_length()) + ' x ' + str(desk.get_width()) + ' x ' + str(desk.get_height()))
    print('Drawer Location: ' + desk.get_drawer_location() + 'Count: ' + str(desk.get_number_drawers()))
    print('Price: ' + "${:0,.2f}".format(desk.get_price()))
# Calls the 'main' function
main()
