# Imports the tkinter module
import tkinter
import tkinter.messagebox


# Defines the 'Menu' Class
class Menu:
    # Defines the __init__ method
    def __init__(self):
        # Creates main window, root object.
        self.main_window = tkinter.Tk()
        self.main_window.title("Pizza Menu")
        # ---------------------------------------------------------------------------------------
        # Creates StringVar objects to display
        self.menu = tkinter.Menu(self.main_window)
        self.itemPrice = tkinter.StringVar()
        self.total_value = 0

        # Creates Frames
        self.item1_frame = tkinter.Frame(self.main_window)
        self.item2_frame = tkinter.Frame(self.main_window)
        self.item3_frame = tkinter.Frame(self.main_window)
        self.item4_frame = tkinter.Frame(self.main_window)
        self.item5_frame = tkinter.Frame(self.main_window)
        self.item6_frame = tkinter.Frame(self.main_window)
        self.item7_frame = tkinter.Frame(self.main_window)
        self.item8_frame = tkinter.Frame(self.main_window)
        self.menu_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.quit_frame = tkinter.Frame(self.main_window)

        # Create and Pack label widgets for Menu Title
        # ---Create
        self.Main_label = tkinter.Label(self.main_window, text='-------------------------------- \n'
                                                               'Pizza Menu: '
                                                               '\n--------------------------------')
        # ---Pack
        self.Main_label.pack(side='top')

        # Create and Pack label widgets for 'items'
        # ****Add Menu Items***
        # ---Create items
        self.item1_label = tkinter.Label(self.item1_frame, text='1) Cheese - $10.99')
        self.item2_label = tkinter.Label(self.item2_frame, text='2) Garlic Tomato - $13.99')
        self.item3_label = tkinter.Label(self.item3_frame, text='3) Pepperoni - $12.99')
        self.item4_label = tkinter.Label(self.item4_frame, text='4) Sausage - $12.99')
        self.item5_label = tkinter.Label(self.item5_frame, text='5) Mushroom - $12.99')
        self.item6_label = tkinter.Label(self.item6_frame, text='6) Supreme - $15.99')
        self.item7_label = tkinter.Label(self.item7_frame, text='Stuffed Crust - $2.99')
        self.item8_label = tkinter.Label(self.item8_frame, text='Double Dough - $1.49')
        # ---Pack items
        self.item1_label.pack(side='left')
        self.item2_label.pack(side='left')
        self.item3_label.pack(side='left')
        self.item4_label.pack(side='left')
        self.item5_label.pack(side='left')
        self.item6_label.pack(side='left')
        self.item7_label.pack(side='left')
        self.item8_label.pack(side='left')

        # Create and Pack label widgets for total
        # ---Create total labels
        self.results_label = tkinter.Label(self.total_frame, text='Total Price: ')
        self.total_label = tkinter.Label(self.total_frame, textvariable=self.total_value)
        # ---Pack total labels
        self.results_label.pack(side='left')
        self.total_label.pack(side='left')

        # Create and Pack Button Widgets
        # ---Create Buttons
        self.item1_button = tkinter.Button(self.item1_frame, text='Add Pizza',
                                           command=self.add_item1)
        self.item2_button = tkinter.Button(self.item2_frame, text='Add Pizza',
                                           command=self.add_item2)
        self.item3_button = tkinter.Button(self.item3_frame, text='Add Pizza',
                                           command=self.add_item3)
        self.item4_button = tkinter.Button(self.item4_frame, text='Add Pizza',
                                           command=self.add_item4)
        self.item5_button = tkinter.Button(self.item5_frame, text='Add Pizza',
                                           command=self.add_item5)
        self.item6_button = tkinter.Button(self.item6_frame, text='Add Pizza',
                                           command=self.add_item6)
        self.item7_button = tkinter.Button(self.item7_frame, text='Add Pizza',
                                           command=self.add_item7)
        self.item8_button = tkinter.Button(self.item8_frame, text='Add Pizza',
                                           command=self.add_item8)
        self.clear_button = tkinter.Button(self.quit_frame, text='Clear Items',
                                           command=self.clear_items)
        self.quit_button = tkinter.Button(self.quit_frame, text='Quit',
                                          command=self.main_window.destroy)
        # ---Pack Buttons
        self.item1_button.pack()
        self.item2_button.pack()
        self.item3_button.pack()
        self.item4_button.pack()
        self.item5_button.pack()
        self.item6_button.pack()
        self.item7_button.pack()
        self.item8_button.pack()
        self.quit_button.pack(side='left')
        self.clear_button.pack(side='right')

        # Pack Frames
        self.menu_frame.pack()
        self.item1_frame.pack()
        self.item2_frame.pack()
        self.item3_frame.pack()
        self.item4_frame.pack()
        self.item5_frame.pack()
        self.item6_frame.pack()
        self.item7_frame.pack()
        self.item8_frame.pack()
        self.total_frame.pack()
        self.quit_frame.pack()

        # Enters the tkinter main loop.
        tkinter.mainloop()

    # Callback function for the 'item1_button' button.
    def add_item1(self):
        self.total_value += 10.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item2_button' button.
    def add_item2(self):
        self.total_value += 13.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item3_button' button.
    def add_item3(self):
        self.total_value += 12.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item4_button' button.
    def add_item4(self):
        self.total_value += 12.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item5_button' button.
    def add_item5(self):
        self.total_value += 12.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item6_button' button.
    def add_item6(self):
        self.total_value += 15.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item7_button' button.
    def add_item7(self):
        self.total_value += 2.99
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'item8_button' button.
    def add_item8(self):
        self.total_value += 1.49
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

    # Callback function for the 'clear_button' button.
    def clear_items(self):
        self.total_value = 0
        self.results_label['text'] = "Total Price: ${:0.2f}".format(self.total_value)

# Create an instance of the PropertyTax class.
my_gui = Menu()
