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


# Display functions
def display_functions():
    print("\nSelect a function:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Exit")


# Get user input and perform calculations
while True:
    display_functions()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        num1 = get_number_input()
        num2 = get_number_input()
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == "2":
        num1 = get_number_input()
        num2 = get_number_input()
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == "3":
        num1 = get_number_input()
        num2 = get_number_input()
        result = multiply(num1, num2)
        print(f"{num1} * {num2}  = {result}")

    elif choice == "4":
        num1 = get_number_input()
        num2 = get_number_input()
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    elif choice == "5":
        num1 = get_number_input()
        result = square(num1)
        print(f"{num1} * {num1} = {result}")

    elif choice == "6":
        print("Exiting the calculator app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
