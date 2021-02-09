# pylint: disable=W0123

'''
DOCSTRING: OOP Calculator using Python
'''

import tkinter as tk
import re # --> Regex used to evaluate the user input inside the program


## Create the calculator class
class Calculator:

    '''
        DOCSTRING: Class Calculator definition
    '''

    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''

        # Assign reference to the main window of the application
        self.master = master

        # Add a name to our application
        master.title("Python Calculator")

        # Create a line where we display the equation
        self.equation=tk.Entry(master, width=50, borderwidth=5)

        # Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Execute the .create_button() method
        self.create_button()



    def create_button(self):

        '''
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        '''

        # Arrange the buttons into lists which represent calculator rows
        row1 = [
                self.add_button(7),
                self.add_button(8),
                self.add_button(9),
                self.add_button('/'),
                self.add_button('c')
        ]
        row2 = [
                self.add_button(4),
                self.add_button(5),
                self.add_button(6),
                self.add_button('*'),
                self.add_button('(')
        ]
        row3 = [
                self.add_button(1),
                self.add_button(2),
                self.add_button(3),
                self.add_button('-'),
                self.add_button(')')
        ]
        row4 = [
                self.add_button(0),
                self.add_button('.'),
                self.add_button('%'),
                self.add_button('+'),
                self.add_button('=')
        ]

        # Assign each button to a particular location on the GUI
        count_row=1
        for row in [row1, row2, row3, row4]:
            count=0
            for button in row:
                button.grid(row=count_row, column=count, columnspan=1)
                count+=1
            count_row+=1


    def add_button(self,value):

        '''
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,%,",",-,*,/,c,=)
        OUTPUT: returns a designed button object
        '''
        if value == '=':
            background_color = "green"
            active_background_color = "green"
        else:
            background_color = None
            active_background_color = None

        return tk.Button(self.master,text=value,width=9,bg=background_color, \
            activebackground=active_background_color, \
            command=lambda:self.click_button(str(value)))


    def click_button(self, value):

        '''
        DOCSTRING: Method that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,%,",",-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        '''

        # Get the equation that's entered by the user
        current_equation=str(self.equation.get())

        # If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, tk.END)

        # If user clicked "=", then compute the answer and display it
        elif value == '=':
            try:
                if "%" in current_equation:
                    operation = re.findall(r'[\-\+\*\/]', current_equation)
                    if operation:
                        answer = current_equation.replace("%","")
                        first_input = re.compile(r'[\-\+\*\/]').split(answer)[0]
                        second_input = re.compile(r'[\-\+\*\/]').split(answer)[1]
                        answer = float(first_input) * (1 - float(second_input) / 100.0)
                    else:
                        answer = str(eval(current_equation.replace("%","/100")))
                else:
                    answer = str(eval(current_equation))
                self.equation.delete(-1, tk.END)
                self.equation.insert(0, answer)
            except ZeroDivisionError:
                print("\nError: Can't divide by 0!!\n")
            except SyntaxError:
                print("\nError: User entered a wrong operator!!\n")

        # If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, tk.END)
            self.equation.insert(0, current_equation+value)
