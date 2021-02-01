'''
DOCSTRING: OOP Calculator using Python
'''

from tkinter import Tk
from calculator_class import Calculator

#Main Execution Script
if __name__=='__main__':

    #This will create the main window for the application
    window = Tk()

    #Tell our calculator class to use this window
    main_screen = Calculator(window)

    window.geometry("400x200")
    window.minsize(width=400, height=200)
    window.maxsize(width=600, height=300)
    #Executable loop on the application, waits for user input
    window.mainloop()
