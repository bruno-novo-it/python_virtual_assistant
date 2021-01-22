from tkinter import *
from calculator_class import Calculator

#Main Execution Script
if __name__=='__main__':

    #This will create the main window for the application
    window = Tk()

    #Tell our calculator class to use this window
    main_screen = Calculator(window)

    #Executable loop on the application, waits for user input
    window.mainloop()