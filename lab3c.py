#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: frajper

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
     A = number1 + number2
     return A
    elif operator == 'subtract':
     B = number1 - number2
     return B
    elif operator == 'multiply':
     C = number1 * number2
     return C
    else:
       return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
