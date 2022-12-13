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
# Value Of Pi
pi = (3.14)
# Telling User What Operations There Is
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Select operation by typing the number")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent/To The Power Of")
print("18. Square Root")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("6. Calculate The Circumference Of A Circle If You Have Diameter")
print("7. Calculate The Circumference Of A Circle If You Have Radius")
print("8. Calculate The Circumference Of A Circle If You Have Area")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("9. Calculate The Area Of A Circle If You Have Diameter")
print("10. Calculate The Area Of A Circle If You Have Radius")
print("11. Calculate The Area Of A Circle If You Have Circumference")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("12. Calculate The Radius Of A Circle If You Have Diameter")
print("13. Calculate The Radius Of A Circle If You Have Area")
print("14. Calculate The Radius Of A Circle If You Have Circumference")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("15. Calculate The Diameter Of A Circle If You Have Radius")
print("16. Calculate The Diameter Of A Circle If You Have Area")
print("17. Calculate The Diameter Of A Circle If You Have Circumference")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
# Gathering Input
while True:
    choice = input("Choice: ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        
# Gathering Input For The Option 6 Because Complicated
    if choice in ('6'):
        diameter = float(input("Diameter: "))
        
        if choice == ('6'):
            print(diameter, "*", pi, "=", (diameter*pi), "(Formula: C = pi*d)")

    if choice in ('7'):
        radius = float(input("Radius: "))
        diameter = (radius*2)
        
        if choice == ('7'):
            print(radius, "*", "2", "=", diameter, "*", pi, "=" (diameter*pi), "Formula: r*2=d*pi=c ")

    if choice in ('8'):
        area = float(input("Area: "))

        if choice == ('8'):
            print("2", "*", "The Square Root Of:", "(",pi, "*", area,")", "=", (2*(pi*area)**0.5), "Formula: 2V--(pi*a)=c (The V-- Is Supposed To Be The Square Root Symbol)")
    
    if choice in ('9'):
        diameter = float(input("Diameter: "))
        radius = (diameter/2)

        if choice == ('9'):
            print(diameter, "/", "2", radius, "^", "2", "*", pi, "=", (radius**2*3.14), "Formula: d/2=r^2*pi=a")

    if choice in ('10'):
        radius = float(input("Radius: "))

        if choice == ('10'):
            print(radius, "^", "2", "*", pi, "="(radius**2*3.14), "Formula: r^2*pi=a")

    if choice in ('11'):
        circumference = float(input("Circumference: "))

        if choice == ('11'):
            print(circumference, "^", "2","/", "4", "*", pi, "=", ((circumference**2)/(4*pi)), "Formula #1: c^2/4*pi=a")
            print("Or Another Way Of Writing The Problem:")
            print(pi,"[",circumference, "/","(","2", pi,"]","^", "2", "=", ((circumference**2)/(4*pi)), "Formula #2: pi[c/(2*pi)]^2=a")

    if choice in ('12'):
        diameter = float(input("Diameter: "))
        radius = (diameter/2)

        if choice == ('12'):
            print(diameter, "/", "2", "=", (radius), "Formula: d/2=r")

    if choice in ('13'):
        area = float(input("Area: "))

        if choice == ('13'):
            print("The Square Root Of:", area, "/", pi, "=", (0.5**(area/pi)), "Formula: a/2*piV-- (The V-- Is Supposed To Be The Square Root Symbol)")

    if choice in ('14'):
        circumference = float(input("Circumference: "))

        if choice == ('14'):
            print(circumference, "/","(","2", "*", pi,")", "=", (circumference/(2*pi)), "Formula: c/2*pi=r")

    if choice in ('15'):
        radius = float(input("Radius: "))

        if choice == (15):
            print(radius, "*", "2", "="(radius*2), "Formula: d/2=r")

    if choice in ('16'):
        area = float(input("Area: "))

        if choice == ('16'):
            print("The Square Root Of:","(",area, "/", pi,")", "=" (0.5**(area/pi)), "Formula: V--(a/pi)=r (The V-- Is Supposed To Be The Square Root Symbol)")
    
    if choice in ('17'):
        circumference = float(input("Circumference: "))
        mystery = (circumference/(2*pi))
        if choice == ('17'):
            print(circumference, "/","(","2", pi, "=", mystery, "*", "2", "=", (mystery*2), "Formula: c/2*pi=?*2=d")

    if choice in ('18'):
        number = float(input("Number: "))

        if choice == ('18'):
            print("The Square Root Of", num1, "=", (num1**0.5), "Formula #1: Number^0.5, Formula #2: V--Number (The V-- Is Supposed To Be The Square Root Symbol)")
            
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
    
    # Exponents/To The Power Of (Shortest) 
    if choice == '5':
        print(num1, "^", num2, "=", (num1**num2))

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
