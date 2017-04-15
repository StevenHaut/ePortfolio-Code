# Defines the 'Office Furniture' Parent Class holds general information about office furniture.


class OfficeFurniture(object):
    """
        The __init__ method accepts category, material, length, width, height, prices
    """
    def __init__(self, category, material, length, width, height, price):

        # Initializes the attributes

        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    # Adds the mutator methods to change the object's value.

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    # Adds accessor methods to return information

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    # Defines the __str__ method and returns the string 'info_string'
    def __str__(self):
        info_string = 'Furniture: ' + self.__category + '  Material: ' + self.__material + "\nLength: " + str(self.__length) + "  Width: " + str(self.__width) + "  Height: " + str(self.__height) + "\nAmount: ${:0,.2f}".format(self.__price) + '\n--------------------------------------------------------'
        return info_string


# Defines the  subclass 'Desk' of the OfficeFurniture class.
class Desk(OfficeFurniture):
    """
        The __init__ method accepts arguments for category, material, length, width, height, prices, drawer_location, and number_drawers
    """
    def __init__(self, category, material, length, width, height, price, drawer_location, number_drawers):
        # Calls the parent class 'OfficeFurniture' and passes arguments to it.
        OfficeFurniture.__init__(self, category, material, length, width, height, price)

        # Initializes the drawer_location and number_drawers

        self.__drawer_location = drawer_location
        self.__number_drawers = number_drawers

    # Adds the mutator methods to change the object's value

    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    # Adds accessor methods to return information

    def get_drawer_location(self):
        return self.__drawer_location

    def get_number_drawers(self):
        return self.__number_drawers

    # Overwrites the __str__ method and returns the string 'info_string'
    def __str__(self):
        info_string = 'Furniture: ' + self.get_category() + '  Material: ' + self.get_material() + "\nLength: " + str(self.get_length()) + "  Width: " + str(self.get_width()) + "  Height:" + str(self.get_height()) + "\nDrawer Location: " + self.__drawer_location + "  Count: " + str(self.__number_drawers) + "\nAmount: ${:0,.2f}".format(self.get_price()) + '\n--------------------------------------------------------'
        return info_string
