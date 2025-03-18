#!/usr/bin/env python
# coding: utf-8

# ### python start 
"""
This is a simple calculator program in Python.
It takes two numbers and an operator as input from the user and performs the respective arithmetic operation.

Functions:
- calculate(num1, num2, operator): Performs the selected operation.

Valid operators:
- '+' for addition
- '-' for subtraction
- '*' for multiplication
- '/' for division (with zero-division handling)
"""

def calculate(num1, num2, operator):
    """Performs basic arithmetic operations based on the given operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error! Division by zero.")
            return None
    else:
        print("Invalid operator!")
        return None

if __name__ == "__main__":
    # Taking input from the user
    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Performing calculation
    result = calculate(num1, num2, operator)
    
    # Displaying the result if valid
    if result is not None:
        print(f"Result: {result:.2f}")


# # intro OPRETERS

# In[ ]:




