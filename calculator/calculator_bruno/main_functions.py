
'''
DOCSTRING: This script contains all necessary functions
SOURCE OF INFORMATION: https://towardsdatascience.com/python-eval-built-in-function-601f87db191
'''

def welcome():
    print("Welcome to Wonderfull World of Calculating!!")

def print_operations():
    print("""
        For operations, just type:
        + for addition
        - for subtraction
        * for multiplication
        / for division
    """)

def calculate():

    first = input('Please enter the first number: ')
    operation = input('Please enter the operation: ')
    second = input('Please enter the second number: ')

    full_operation = first+operation+second

    if operation in ('+','-','*','/'):
        expression = eval(full_operation)
        print()
        print("The results is: {}".format(expression))
        print()
    else:
        print()
        print('You have not typed a valid operator, please run the program again.')
        print()
