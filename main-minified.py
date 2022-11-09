_B='Another? Y/N: ' # Minified spc-0.3
_A='='
from pdb import Restart
def add(x,y):return x+y
def subtract(x,y):return x-y
def multiply(x,y):return x*y
def divide(x,y):return x/y
print('Select operation by typing the number')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Exponent/To The Power Of')
print('For Choice 5, I made the program solve the (to the power of) using multiplication, so thats why the output shows a multiplication star.')
while True:
	choice=input('Input:')
	if choice in('1','2','3','4','5'):num1=float(input('First Number:'));num2=float(input('Second Number:'));num3=float(multiply(num1,num2))
	if choice=='1':print(num1,'+',num2,_A,add(num1,num2))
	if choice=='2':print(num1,'-',num2,_A,subtract(num1,num2))
	if choice=='3':print(num1,'*',num2,_A,multiply(num1,num2))
	if choice=='4':print(num1,'/',num2,_A,divide(num1,num2))
	if choice=='5':print(num1**num2)
	next_calculation=input(_B)
	if next_calculation=='N':break
	if next_calculation=='Y':Restart
	if next_calculation=='n':break
	if next_calculation=='y':Restart
	else:print("Invalid Input (Type Y Meaning Yes And N Meaning No, Not The Full Word Because The Program Won't Recognize The Input :)");next_calculation=input(_B)