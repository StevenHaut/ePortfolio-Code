# Imports the tkinter module
import tkinter
import tkinter.messagebox


# Defines the 'PropertyTax' Class
class PropertyTax:
    # Defines the __init__ method
    def __init__(self):
        # Creates main window, root object.
        self.main_window = tkinter.Tk()
        self.main_window.title("Property Tax Calculator")

        # Creates StringVar objects to display
        self.assessmentValue = tkinter.StringVar()
        self.propertyTax = tkinter.StringVar()

        # Creates 4 Frames
        self.actualValue_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.assessmentValue_frame = tkinter.Frame(self.main_window)
        self.propertyTax_frame = tkinter.Frame(self.main_window)

        # Create and Pack label & entry widgets for 'actualValue'
        self.actualValue_label = tkinter.Label(self.actualValue_frame,
                                               text='Enter the Actual Value of a Property: ')
        self.actualValue_entry = tkinter.Entry(self.actualValue_frame, width=10)
        self.actualValue_label.pack(side='left')
        self.actualValue_entry.pack(side='left')

        # Create and Pack label widgets for 'assessmentValue'
        self.result_label = tkinter.Label(self.assessmentValue_frame, text='Assessment Value: ')
        self.assessmentValue_label = tkinter.Label(self.assessmentValue_frame, textvariable=self.assessmentValue)
        self.result_label.pack(side='left')
        self.assessmentValue_label.pack(side='left')

        # Create and Pack label widgets for 'propertyTax'
        self.result2_label = tkinter.Label(self.propertyTax_frame, text='Property Tax: ')
        self.propertyTax_label = tkinter.Label(self.propertyTax_frame, textvariable=self.propertyTax)
        self.result2_label.pack(side='left')
        self.propertyTax_label.pack(side='left')

        # Create and Pack button widgets
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.actualValue_frame.pack()
        self.assessmentValue_frame.pack()
        self.propertyTax_frame.pack()
        self.button_frame.pack()

        # Enters the tkinter main loop.
        tkinter.mainloop()

    # Callback function for the 'calc_button' button.
    def calculate(self):
        value = float(self. actualValue_entry.get())
        # Calculate Assessment Value
        self.assessmentValue = value * 0.60

        # Calculate Property Tax
        self.propertyTax = self.assessmentValue * 0.0075

        # Adjust result labels
        self.result_label['text'] = "Assessment Value: ${:0.2f}".format(self.assessmentValue)
        self.result2_label['text'] = "Property Tax: ${:0.2f}".format(self.propertyTax)

# Create an instance of the PropertyTax class.
my_gui = PropertyTax()
