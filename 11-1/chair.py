# Imports the program "officeFurniture"
import officeFurniture


# Defines the function 'main'
def main():
    # Creating an object of the OfficeFurniture class
    chair = officeFurniture.OfficeFurniture('Black Office Chair ', 'Steel(frame) and Mesh', 28, 30, 44, 300.00)

    # Displays the returned string containing the information
    print(chair)

    # Displays the information
    print('Furniture: ' + chair.get_category())
    print('Material: ' + chair.get_material())
    print('Dimensions(L x W x H): ' + str(chair.get_length()) + ' x ' + str(chair.get_width()) + ' x ' + str(chair.get_height()))
    print('Price: ' + "${:0,.2f}".format(chair.get_price()))
# Calls the 'main' function
main()
