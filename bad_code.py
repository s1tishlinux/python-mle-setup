"""
Module: bad_code.py
Description: A simple arithmetic operations module that demonstrates addition, subtraction, multiplication, and division.
"""


def add(x, y):
    """
    Function: add
    Description: Adds two numbers together.
    Args:
    - x (int or float): The first number.
    - y (int or float): The second number.
    Returns:
    - int or float: The sum of x and y.
    """
    return x + y


def sub(x, y):
    """
    Function: sub
    Description: Subtracts the second number from the first number.
    Args:
    - x (int or float): The first number.
    - y (int or float): The second number.
    Returns:
    - int or float: The result of x - y.
    """
    return x - y


def multiply(x, y):
    """
    Function: multiply
    Description: Multiplies two numbers together.
    Args:
    - x (int or float): The first number.
    - y (int or float): The second number.
    Returns:
    - int or float: The product of x and y.
    """
    z = x * y
    return z


def divide(x, y):
    """
    Function: divide
    Description: Divides the first number by the second number.
    Args:
    - x (int or float): The numerator.
    - y (int or float): The denominator.
    Returns:
    - float: The result of x / y.
    Raises:
    - ZeroDivisionError: If y is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
