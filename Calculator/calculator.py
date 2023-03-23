from calc_art import logo, op_symbols
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }

def calc():
    print(logo)
    try:
        num1 = float(input('What\'s the first number?: '))
        while True:
            print(op_symbols)
            op_user = input('Pick an operation: ')
            num2 = float(input('What\'s the next number?: '))
            result = operations[op_user](num1, num2)
            print(f"{num1} {op_user} {num2} = {result}")
            continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            if continue_calc == 'y':
                num1 = result
            else:
                os.system('cls')
                calc()
    except:
        will_continue = input('Invalid input. If you wish to exit, type \'quit\'. Otherwise, hit the enter key to restart ')
        if will_continue == 'quit':
            quit()
        os.system('cls')
        calc()

calc()
print('\nThank you for using the calculator! Good bye.')

