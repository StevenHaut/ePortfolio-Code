# Imports the tkinter module
import tkinter


# Defines the 'SpanToEngGUI' Class
class SpanToEngGUI:
    # Defines the __init__ method
    def __init__(self):
        # Creates main window, root object.
        self.main_window = tkinter.Tk()

        # Creates StringVar objects to display num1-num5.
        self.num1_value = tkinter.StringVar()
        self.num2_value = tkinter.StringVar()
        self.num3_value = tkinter.StringVar()
        self.num4_value = tkinter.StringVar()
        self.num5_value = tkinter.StringVar()

        # Creates 2 frames (translations, buttons)
        self.translation_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Creates the label widgets
        self.Eng_label = tkinter.Label(self.main_window, text='English Translation:')
        self.Span_label = tkinter.Label(self.button_frame, text='Spanish Words:')
        # num1 - num5 are associated with the StringVar objects.
        self.num1_label = tkinter.Label(self.translation_frame, textvariable=self.num1_value)
        self.num2_label = tkinter.Label(self.translation_frame, textvariable=self.num2_value)
        self.num3_label = tkinter.Label(self.translation_frame, textvariable=self.num3_value)
        self.num4_label = tkinter.Label(self.translation_frame, textvariable=self.num4_value)
        self.num5_label = tkinter.Label(self.translation_frame, textvariable=self.num5_value)

        # Packs the labels
        self.Eng_label.pack(side='top')
        self.Span_label.pack(side='top')
        self.num1_label.pack(side='left')
        self.num2_label.pack(side='left')
        self.num3_label.pack(side='left')
        self.num4_label.pack(side='left')
        self.num5_label.pack(side='left')

        # Creates the button widgets.
        self.num1_button = tkinter.Button(self.button_frame, text='Uno', command=self.show_num1)
        self.num2_button = tkinter.Button(self.button_frame, text='Dos', command=self.show_num2)
        self.num3_button = tkinter.Button(self.button_frame, text='Tres', command=self.show_num3)
        self.num4_button = tkinter.Button(self.button_frame, text='Cuatro', command=self.show_num4)
        self.num5_button = tkinter.Button(self.button_frame, text='Cinco', command=self.show_num5)

        # Packs the buttons.
        self.num1_button.pack(side='left')
        self.num2_button.pack(side='left')
        self.num3_button.pack(side='left')
        self.num4_button.pack(side='left')
        self.num5_button.pack(side='left')

        # Packs the frames.
        self.translation_frame.pack()
        self.button_frame.pack()

        # Enters the tkinter main loop.
        tkinter.mainloop()

    # Callback functions for the Show Info button.

    def show_num1(self):
        self.num1_value.set('One')

    def show_num2(self):
        self.num2_value.set('Two')

    def show_num3(self):
        self.num3_value.set('Three')

    def show_num4(self):
        self.num4_value.set('Four')

    def show_num5(self):
        self.num5_value.set('Five')


# Create an instance of the MyGUI class.
my_gui = SpanToEngGUI()
