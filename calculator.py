#!/usr/bin/python3
def get_number_input():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract y from x
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide x by y, handles division by zero
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


# Function to calculate the square of a number
def square(x):
    return x ** 2


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
