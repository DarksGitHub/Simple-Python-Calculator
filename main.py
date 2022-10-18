# Simple Python Calculator By Darkk#1101

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

# Telling User What Operations There Is
print("Select operation by typing the number")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Gathering Input
while True:
    choice = input("Input:")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("First Number:"))
        num2 = float(input("Second Number:"))

    # Addition (1)
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    # Subtraction (2)
    if choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    # Multiplication (3)
    if choice == '3':
        print(num1, "⋅", num2, "=", multiply(num1, num2))

    # Division (4)
    if choice == '4':
        print(num1, "÷", num2, "=", divide(num1, num2))

    # For Another Calculation
    next_calculation = input("Another? Y/N")
    if next_calculation == "N":
        break

    # Invalid Input For "inputs" Not Compatible With The Code
    else:
        print("Invalid Input")