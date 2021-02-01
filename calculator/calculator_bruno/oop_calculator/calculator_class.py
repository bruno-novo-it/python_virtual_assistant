'''
DOCSTRING: OOP Calculator using Python
'''

import tkinter as tk

## Create the calculator class
class Calculator:

    '''
        DOCSTRING: Class Calculator definition
    '''

    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''

        #Assign reference to the main window of the application
        self.master = master

        #Add a name to our application
        master.title("Python Calculator")

        #Create a line where we display the equation
        self.equation=tk.Entry(master, width=36, borderwidth=5)

        #Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Execute the .creteButton() method
        self.create_button()



    def create_button(self):

        '''
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        '''

        #We first create each button one by one with the value we want
        #Using add_button() method which is described below
        button_0 = self.add_button(0)
        button_1 = self.add_button(1)
        button_2 = self.add_button(2)
        button_3 = self.add_button(3)
        button_4 = self.add_button(4)
        button_5 = self.add_button(5)
        button_6 = self.add_button(6)
        button_7 = self.add_button(7)
        button_8 = self.add_button(8)
        button_9 =  self.add_button(9)
        button_add = self.add_button('+')
        button_sub = self.add_button('-')
        button_mult = self.add_button('*')
        button_div = self.add_button('/')
        button_clear = self.add_button('c')
        button_equal = self.add_button('=')

        #Arrange the buttons into lists which represent calculator rows
        row1=[button_7,button_8,button_9,button_add]
        row2=[button_4,button_5,button_6,button_sub]
        row3=[button_1,button_2,button_3,button_mult]
        row4=[button_clear,button_0,button_equal,button_div]

        #Assign each button to a particular location on the GUI
        count_row=1
        for row in [row1, row2, row3, row4]:
            count=0
            for buttn in row:
                buttn.grid(row=count_row, column=count, columnspan=1)
                count+=1
            count_row+=1


    def add_button(self,value):

        '''
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        '''
        return tk.Button(self.master,text=value,width=9,command=lambda: self.click_button(str(value)))


    def click_button(self, value):

        '''
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        '''

        #Get the equation that's entered by the user
        current_equation=str(self.equation.get())

        #If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, tk.END)

        #If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, tk.END)
            self.equation.insert(0, answer)

        #If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, tk.END)
            self.equation.insert(0, current_equation+value)
