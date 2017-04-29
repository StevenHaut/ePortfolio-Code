# Imports the tkinter module
import tkinter
import tkinter.messagebox


# Defines the 'CalculateMPG' Class
class CalculateMPG:
    # Defines the __init__ method
    def __init__(self):
        # Creates main window, root object.
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        # Creates StringVar objects to display MPG(miles per gallon)
        self.mpg_value = tkinter.StringVar()

        # Creates 4 Frames (gallons, miles, button, mpg)
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)

        # Create and Pack label & entry widgets for Gallons
        self.gallons_label = tkinter.Label(self.gallons_frame, text='Enter # of Gallons of Gas: ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Create and Pack label & entry widgets for Miles
        self.miles_label = tkinter.Label(self.miles_frame, text='Enter # Miles Driven on Full Tank: ')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create and Pack label widgets for MPG
        self.result_label = tkinter.Label(self.mpg_frame, text='MPG: ')
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg_value)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # Create and Pack button widgets
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate MPG ', command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.button_frame.pack()
        self.mpg_frame.pack()

        # Enters the tkinter main loop.
        tkinter.mainloop()

    # Callback function for the 'calc_button' button.
    def calc_mpg(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        # Calculate Miles per Gallon
        self.mpg_value = miles / gallons
        self.result_label['text'] = "MPG: {:0.1f}".format(self.mpg_value)

# Create an instance of the CalculateMPG class.
my_gui = CalculateMPG()
