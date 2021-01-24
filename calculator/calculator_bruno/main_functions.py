
'''
DOCSTRING: This script contains all necessary functions
SOURCE OF INFORMATION: https://towardsdatascience.com/python-eval-built-in-function-601f87db191
                       https://regex101.com/
'''

import os # --> Used for clean the terminal after run the calculator again
import sys # --> Used for finish the process and exit the script
import re # --> Regex used to evaluate the user input inside the program

## Welcome message
def welcome():
    print("Welcome to Wonderfull World of Calculating!!")

## Print all operations
def print_operations():
    print("""
        For operations, just type:
        + for addition
        - for subtraction
        * for multiplication
        / for division
    """)

## Primary calculate function
def calculate():

    # Clear the screen
    os.system('cls||clear')

    # Call info functions
    welcome()
    print_operations()

    # Variables definition
    first = None
    second = None
    operation = None

    # User input
    first = input("Please enter the first number: ")
    while bool(re.match(r"^-?\d+\.?\d*$",first)) is False:
        print()
        print("You have not typed a valid number! Please, try again")
        print()
        first = input("Please enter the first number: ")
        print()



    operation = input('Please enter the operation: ')
    second = input('Please enter the second number: ')

    # Build the full operation
    full_operation = first+operation+second

    if operation in ('+','-','*','/'):
        expression = eval(full_operation)
        print()
        print("The results is: {}".format(expression))
        print()
    else:
        print()
        print("You haven't typed a valid operator, please run the program again.")
        print()
        sys.exit("Exiting...")

    run_again()

## Run the script again
def run_again():
    keep_calculating = input("""To calculate again, please type Y/y for Yes or N/n for No: """)

    if keep_calculating.upper() in ('Y','N'):
        # The input can be 'y' or 'Y'
        if keep_calculating.upper() == 'Y':
            calculate()
        # The input can be 'n' or 'N'
        elif keep_calculating.upper() == 'N':
            print()
            print("Bye Bye! See you later.")
        else:
            run_again()
    else:
        print()
        print('You have not typed a valid answer! Please, type Y/y ou N/n.')
        print()
        run_again()
