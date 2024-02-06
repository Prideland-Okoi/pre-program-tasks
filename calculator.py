#!/usr/bin/python3

def get_number_input():
    """
    Function to get a valid numerical input from the user.
    """
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add(x, y):
    """
    Function to add two numbers.
    """
    return x + y


def subtract(x, y):
    """
    Function to subtract y from x.
    """
    return x - y


def multiply(x, y):
    """
    Function to multiply two numbers.
    """
    return x * y


def divide(x, y):
    """
    Function to divide x by y, handles division by zero.
    """
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def square(x):
    """
    Function to calculate the square of a number.
    """
    return x ** 2


def calculator():
    """
    Main function to perform arithmetic operations based on user input.
    """
    while True:
        num1 = get_number_input()
        operation = input(
            "Select operation: + (add), - (subtract), * (multiply), / (divide), ** (square), or 'q' to quit: ")

        if operation.lower() == 'q':
            break

        if operation in ('+', '-', '*', '/'):
            num2 = get_number_input()
        else:
            num2 = None

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '**':
            result = square(num1)
        else:
            print("Invalid operation selected. Please try again.")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    calculator()
