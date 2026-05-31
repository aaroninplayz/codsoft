import math
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
unit=1
acc=2
while True:
    print("--welcome to the calculator--")
    print("please choose the appropriate category of calculation you want to perform:")
    print ("1.arthmetic calculator:")
    print ("2.advanced calculator:")
    print ("3.trignometric calculator:")
    print ("4.settings:")
    print ("5.documentation:")
    print ("6.exit:")
    c=int(input("enter your choice: "))
    if c==1:
        clear()
        while True:
            print("1.addition")
            print("2.subtraction")
            print("3.multiplication")
            print("4.division")
            print("5.back to main menu")
            c1=int(input("enter your choice: "))
            if c1==1:
                try:
                    x=float(input("enter the first number: "))
                    y=float(input("enter the second number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                print(round(x+y, acc))
                input()
                clear()
            elif c1==2:
                try:
                    x=float(input("enter the first number: "))
                    y=float(input("enter the second number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                print(round(x-y, acc))
                input()
                clear()
            elif c1==3:
                try:
                    x=float(input("enter the first number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                y=float(input("enter the second number: "))
                print(round(x*y, acc))
                input()
                clear()
            elif c1==4:
                try:
                    x=float(input("enter the first number: "))
                    y=float(input("enter the second number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                if y==0:
                    print("division by zero is not allowed")
                else:
                    print(round(x/y, acc))
                    input()
                    clear()
            elif c1==5:
                break
            else:
                print("invalid choice")       
    elif c==2:
        clear()
        while True:
            print("1.power")
            print("2.exponential")
            print("3.logarithm")
            print("4.root")
            print("5.back to main menu")
            c2=int(input("enter your choice: "))
            if c2==1:
                try:
                    x=float(input("enter the main number: "))
                    y=float(input("enter the power too which it must be raised too: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                print(round(math.pow(x,y), acc))
                input()
                clear()
            elif c2==2:
                try:
                    x=float(input("enter the number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                print(round(math.exp(x), acc))
                input()
                clear()
            elif c2==3:
                try:
                    x=float(input("enter the number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                if x<=0:
                    print("logarithm is only defined for positive numbers")
                else:
                    print(round(math.log(x), acc))
                    input()
                    clear()
            elif c2==4:
                try:
                    x=float(input("enter the number: "))
                    y=float(input("enter the root: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                if y==0:
                    print("root cannot be zero")
                else:
                    print(round(math.pow(x,1/y), acc))
                    input()
                    clear()
            elif c2==5:
                break
            else:
                print("invalid choice")
    elif c==3:
        clear()
        while True:
            print("1.sine")
            print("2.cosine")
            print("3.tangent")
            print("4.cotangent")
            print("5.secant")
            print("6.cosecant")
            print("7.back to main menu")
            if unit==1:
                try:
                    x=float(input("enter the angle in degree: "))
                    x=math.radians(x)
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
            else:
                try:
                    x=float(input("enter the angle in radian: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
            c2=int(input("choose the trignometric function: "))
            if c2==1:
                print(round(math.sin(x), acc))
                input()
                clear() 
            elif c2==2:
                print(round(math.cos(x), acc))
                input()
                clear()
            elif c2==3:
                print(round(math.tan(x), acc))
                input()
                clear()
            elif c2==4:
                if abs(math.tan(x)) < 1e-10:
                    print("cotangent undefined")
                else:
                    print(round(1/math.tan(x), acc))
                input()
                clear()
            elif c2==5:
                if abs(math.cos(x)) < 1e-10:
                    print("secant undefined")
                else:
                    print(round(1/math.cos(x), acc))
                input()
                clear()
            elif c2==6:
                if abs(math.sin(x)) < 1e-10:
                    print("cosecant undefined")
                else:
                    print(round(1/math.sin(x), acc))
                input()
                clear()
            elif c2==7:
                break
            else:
                print("invalid choice")   
    elif c==4:
        clear()
        while True:
            print("1.accuracy settings:")
            print("2.angle unit settings:")
            print("3.back to main menu:")
            c3=int(input("enter your choice: "))
            if c3==1:
                while True:
                    acc=int(input("enter the number of decimal places you want to round off to: "))
                    if acc < 0:
                        print("invalid input. please enter a positive integer.")
                        input()
                        clear()
                    else:
                        print("accuracy set to",acc,"decimal places")
                        break
            elif c3==2:
                while True:
                    unit=int(input("enter the unit (1 for degree, 2 for radian): "))
                    if unit==1:
                        print("angle unit set to degree")
                        input()
                        clear()
                        break
                    elif unit==2:
                        print("angle unit set to radian")
                        input()
                        clear()
                        break
                    else:
                        print("invalid choice")
            elif c3==3:
                break
            else:
                print("invalid choice")
    elif c==5:
        print("""
          
=========================
CALCULATOR DOCUMENTATION
=========================

OVERVIEW
--------
This calculator is a menu-driven Python application that provides
three categories of mathematical operations:

1. Arithmetic Calculations
2. Advanced Calculations
3. Trigonometric Calculations

The program also allows users to customize calculation accuracy
and angle units through the Settings menu.

--------------------------------------------------

1. ARITHMETIC CALCULATOR
------------------------
Performs basic mathematical operations on two numbers.

Available operations:
- Addition
- Subtraction
- Multiplication
- Division

Note:
Division by zero is not allowed and will display an error message.

--------------------------------------------------

2. ADVANCED CALCULATOR
----------------------
Provides higher-level mathematical functions.

Available operations:
- Power (x^y)
- Exponential (e^x)
- Natural Logarithm (ln(x))
- Nth Root (x^(1/y))

Important Notes:
- Logarithm is only defined for positive numbers.
- Roots of negative numbers may produce invalid results depending
  on the root value.

--------------------------------------------------

3. TRIGONOMETRIC CALCULATOR
---------------------------
Calculates values of common trigonometric functions.

Available functions:
- Sine (sin)
- Cosine (cos)
- Tangent (tan)
- Cotangent (cot)
- Secant (sec)
- Cosecant (csc)

Supported angle units:
- Degrees
- Radians

The angle unit can be changed in the Settings menu.

Warning:
Some trigonometric functions are undefined for specific angles and
may result in errors or very large values.

--------------------------------------------------

4. SETTINGS
-----------
Accuracy Settings:
Allows the user to specify the number of decimal places used when
displaying results.

Examples:
Accuracy = 2 -> 3.14
Accuracy = 4 -> 3.1416

Angle Unit Settings:
1 -> Degrees
2 -> Radians

Default Unit: Degrees

--------------------------------------------------

5. DOCUMENTATION
----------------
Displays information about the calculator, available features,
settings, and usage guidelines.

--------------------------------------------------

6. EXIT
-------
Terminates the calculator program.

--------------------------------------------------

DEFAULT SETTINGS
----------------
Accuracy   : 2 Decimal Places
Angle Unit : Degrees

--------------------------------------------------

ERROR HANDLING
--------------
The calculator includes basic error handling for:
- Invalid menu choices
- Division by zero

Users should enter valid numerical values when prompted.

--------------------------------------------------

DEVELOPED USING
---------------
Python 3
math module

Version: Calculator v1.0

Thank you for using the Calculator!
""")
        input()
        clear()
    elif c==6:
        print("exiting the calculator...")
        break
