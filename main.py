# Simple Python Calculator By Darkk#1101

# For The "Another Y/N?" Y Option To Restart The Code
from pdb import Restart
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
print("5. Exponent/To The Power Of")
print("For Choice 5, I made the program solve the (to the power of) using multiplication, so thats why the output shows a multiplication star.")

# Gathering Input
while True:
    choice = input("Input:")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("First Number:"))
        num2 = float(input("Second Number:"))
        num3 = float(multiply(num1, num2))
    # Addition (1)
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    # Subtraction (2)
    if choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    # Multiplication (3)
    if choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    # Division (4)
    if choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    
    # Exponents/To The Power Of (5) 
    if choice == '5':
        print(num1**num2)
    # For Another Calculation
    next_calculation = input("Another? Y/N: ")
    if next_calculation == "N":
        break
    if next_calculation == "Y":
        Restart
    if next_calculation == "n":
        break
    if next_calculation == "y":
        Restart
    # Invalid Input For "inputs" Not Compatible With The Code
    else:
        print("Invalid Input (Type Y Meaning Yes And N Meaning No, Not The Full Word Because The Program Won't Recognize The Input :)")
        next_calculation = input("Another? Y/N: ")
