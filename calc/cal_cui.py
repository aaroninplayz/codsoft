import math
import os
def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print("\n" * 100)
unit=1
acc=2
hys=[]
o=3
def h(w):
    if len(hys)==o:
        hys.remove(hys[0])
        hys.append(w)
    else:
        hys.append(w)

while True:
    clear()
    print("--welcome to the calculator--")
    print("please choose the appropriate category of calculation you want to perform:")
    print ("1.arithmetic calculator:")
    print ("2.advanced calculator:")
    print ("3.trigonometric calculator:")
    print ("4.show history:")
    print ("5.settings:")
    print ("6.how to use:")
    print ("7.documentation:")
    print ("8.exit:")
    try:
        c=int(input("enter your choice: "))
    except ValueError:
        print("invalid input. please enter a valid number.")
        input()
        clear()
        continue
    if c==1:
        clear()
        while True:
            print("1.addition")
            print("2.subtraction")
            print("3.multiplication")
            print("4.division")
            print("5.back to main menu")
            try:
                c1=int(input("enter your choice: "))
            except ValueError:
                print("invalid input. please enter a valid number.")
                input()
                clear()
                continue
            if c1==1:
                try:
                    x=float(input("enter the first number: "))
                    y=float(input("enter the second number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                r=round(x+y, acc)
                w="{} + {} = {}".format(x, y, r)
                h(w)
                print(w)
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
                r=round(x-y, acc)
                w="{} - {} = {}".format(x, y, r)
                h(w)
                print(w)
                input()
                clear()
            elif c1==3:
                try:
                    x=float(input("enter the first number: "))
                    y=float(input("enter the second number: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                r=round(x*y, acc)
                w="{} * {} = {}".format(x, y, r)
                h(w)
                print(w)
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
                    r=round(x/y, acc)
                    w="{} / {} = {}".format(x, y, r)
                    h(w)
                    print(w)
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
            try:
                c2=int(input("enter your choice: "))
            except ValueError:
                print("invalid input. please enter a valid number.")
                input()
                clear()
                continue
            if c2==1:
                try:
                    x=float(input("enter the main number: "))
                    y=float(input("enter the power to which it must be raised too: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                try:
                    r=round(math.pow(x,y), acc)
                    w="{} ^ {} = {}".format(x, y, r)
                    h(w)
                    print(w)
                except  OverflowError:
                    print("result is too large to handle")
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
                try:
                    r=round(math.exp(x), acc)
                    w="e ^ {} = {}".format(x, r)
                    h(w)
                    print(w)
                except  OverflowError:
                    print("result is too large to handle")
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
                    input()
                    clear()
                else:
                    r=round(math.log(x), acc)
                    w="log({}) = {}".format(x,r)
                    h(w)
                    print(w)
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
                    try:
                        r=round(math.pow(x,1/y), acc)
                        w="{} ^ (1/{}) = {}".format(x, y, r)
                        h(w)
                        print(w)
                    except  ValueError:
                        print("result is invalid")
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
            try:
                c2=int(input("choose the trigonometric function you want to calculate: "))
            except ValueError:
                print("invalid input. please enter a valid number.")
                input()
                clear()
                continue
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
            if c2==1:
                r=round(math.sin(x), acc)
                w="sin({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                h(w)
                print(w)
                input()
                clear() 
            elif c2==2:
                r=round(math.cos(x), acc)
                w="cos({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                h(w)
                print(w)
                input()
                clear()
            elif c2==3:
                if abs(math.cos(x)) < 1e-10:
                    print("tangent undefined")
                else:
                    r=round(math.tan(x), acc)
                    w="tan({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                    h(w)
                    print(w)
                    input()
                    clear()
            elif c2==4:
                if abs(math.tan(x)) < 1e-10:
                    print("cotangent undefined")
                else:
                    r=round(1/math.tan(x), acc)
                    w="cot({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                    h(w)
                    print(w)
                input()
                clear()
            elif c2==5:
                if abs(math.cos(x)) < 1e-10:
                    print("secant undefined")
                else:
                    r=round(1/math.cos(x), acc)
                    w="sec({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                    h(w)
                    print(w)
                input()
                clear()
            elif c2==6:
                if abs(math.sin(x)) < 1e-10:
                    print("cosecant undefined")
                else:
                    r=round(1/math.sin(x), acc)
                    w="csc({}) = {}".format(math.degrees(x) if unit == 1 else x, r)
                    h(w)
                    print(w)
                input()
                clear()
            elif c2==7:
                break
            else:
                print("invalid choice")   
    elif c==5:
        clear()
        while True:
            print("1.accuracy settings:")
            print("2.angle unit settings:")
            print("3.history:")
            print("4.back to main menu:")
            try:
                c3=int(input("enter your choice: "))
            except ValueError:
                print("invalid input. please enter a valid number.")
                input()
                clear()
                continue
            if c3==1:
                while True:
                    try:
                        acc=int(input("enter the number of decimal places you want to round off to: "))
                        if acc < 0:
                            print("accuracy cannot be negative")
                            continue
                        print(f"accuracy set to {acc} decimal places")
                        input()
                        clear()
                        break
                    except ValueError:  
                        print("invalid input. please enter a valid positive number.")
                        input()
                        clear()
                        continue
            elif c3==2:
                while True:
                    try:
                        unit=int(input("enter the unit (1 for degree, 2 for radian): "))
                    except ValueError:
                        print("invalid input. please enter a valid number.")
                        input()
                        clear()
                        continue
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
                print("1.show History:")
                print("2.clear history:")
                print("3.history settings:")
                try:
                    c4=int(input("enter your choice: "))
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    input()
                    clear()
                    continue
                if c4==1:
                    if len(hys)==0:
                        print("history is empty")
                    else:
                        print("calculation history:")
                        for i, item in enumerate(hys, 1):
                            print(f"{i}. {item}")
                    input()
                    clear()
                elif c4==2:
                    hys.clear()
                    print("history cleared")
                    input()
                    clear()
                elif c4==3:
                    print("history settings:")
                    print(f"current history size: {o}")
                    while True:
                        try:
                            o=int(input("enter the new history size (positive integer): "))
                            if o <= 0:
                                print("history size must be a positive integer")
                                continue
                            print(f"history size set to {o}")
                            while len(hys)>o:
                                hys.remove(hys[0])  
                            input()
                            clear()
                            break
                        except ValueError:
                            print("invalid input. please enter a valid positive integer.")
                            input()
                            clear()
                            continue
            elif c3==4:
                break
            else:
                print("invalid choice")
    elif c==7:
        print("""=========================
CALCULATOR DOCUMENTATION
========================

## OVERVIEW

Python Calculator v3.0 is a menu-driven command-line application developed to provide arithmetic, advanced mathematical, and trigonometric calculations through a structured and user-friendly interface.

The calculator emphasizes reliability, configurability, input validation, exception handling, and calculation history management.

---

## FEATURES

Arithmetic Operations
• Addition
• Subtraction
• Multiplication
• Division

Advanced Operations
• Power Calculations
• Exponential Functions
• Natural Logarithms
• Root Calculations

Trigonometric Operations
• Sine
• Cosine
• Tangent
• Cotangent
• Secant
• Cosecant

History Management
• Automatic calculation tracking
• View history
• Clear history
• Configurable history size

User Settings
• Accuracy configuration
• Degree/Radian mode selection
• History configuration

System Features
• Cross-platform screen clearing
• Extensive input validation
• Exception handling
• Menu-driven architecture

---

## CALCULATION HISTORY

Version 3.0 introduces a dedicated calculation history system.

Each successful calculation is stored in memory and can be reviewed at any time.

History Features:

• Stores recent calculations
• Configurable maximum capacity
• Automatic removal of oldest entries when capacity is reached
• Manual history clearing
• Accessible from both the main menu and settings menu

History remains available during the current program session and is cleared when the application terminates.

---

## SETTINGS MODULE

The Settings Module allows customization of calculator behavior.

Accuracy Management
• Controls decimal precision of displayed results.
• Negative values are rejected.

Angle Unit Management
• Degree Mode
• Radian Mode

History Configuration
• Modify maximum history size.
• Clear history records.
• Display stored calculations.

---

## EXCEPTION HANDLING

ValueError Handling
• Invalid numerical inputs
• Invalid menu selections
• Invalid mathematical domains

Division By Zero Protection
• Prevents illegal division operations.

Logarithm Validation
• Ensures logarithms are only calculated for positive values.

Root Validation
• Prevents invalid root calculations.
• Rejects zero roots.

Overflow Protection
• Detects excessively large numerical results.
• Prevents application crashes caused by OverflowError.

Trigonometric Validation
• Detects undefined tangent values.
• Detects undefined cotangent values.
• Detects undefined secant values.
• Detects undefined cosecant values.

Cross-Platform Console Handling
• Attempts operating-system-specific screen clearing.
• Falls back to blank-line clearing if necessary.

---

## PROGRAM STRUCTURE

Modules Used
• math
• os

Core Components
• Main Menu System
• Arithmetic Module
• Advanced Mathematics Module
• Trigonometric Module
• History Management Module
• Settings Module
• Documentation Module

Helper Functions
• clear() – Console management
• h() – History management

---

## DEFAULT CONFIGURATION

Accuracy Setting : 2 Decimal Places
Angle Unit       : Degrees
History Size     : 3 Records

---

## LEARNING OBJECTIVES

This project demonstrates practical implementation of:

• Variables and Data Types
• Conditional Statements
• Loops
• Functions
• Lists
• Exception Handling
• Input Validation
• Mathematical Computation
• Menu-Driven Programming
• User Configuration Management
• History Management Systems
• Cross-Platform Development Concepts

VERSION INFORMATION
-------------------
Application Name : Python Calculator
Version          : 1.1
Language         : Python 3
Modules Used     : math, os
Platform Support : Windows, Linux, macOS

Developer        : Aaron Shibu Mammen
Course           : Bachelor of Engineering (B.E)
Branch           : Computer Science and Engineering (CSE)
Year             : First Year

              

## AREAS OF INTEREST

• Programming
• Software Development
• User Interface (UI) Design
• User Experience (UX) Design
• Artificial Intelligence (AI)
• Machine Learning
• Data Science
• Automation
• Cybersecurity
• Web Development
• Application Development
• Software Engineering
• Problem Solving
• Open Source Development
• Computer Science Fundamentals


--------------------------------------------------

END OF DOCUMENTATION
--------------------------------------------------

Thank you for using the Python Calculator.
""")
        input()
        clear()
    elif c==8:
        print("exiting the calculator...")
        break
    elif c==4:
        clear()
        if len(hys)==0:
            print("history is empty")
        else:
            print("calculation history:")
            for i, item in enumerate(hys, 1):
                print(f"{i}. {item}")
        input()
        clear()
    elif c==6:
        print("""=========================
HOW TO USE THE CALCULATOR
=========================

## OVERVIEW

This calculator is a menu-driven command-line application that allows users to perform arithmetic, advanced mathematical, and trigonometric calculations. The application also includes configurable settings, calculation history management, and comprehensive error handling.

---

## GETTING STARTED

1. Launch the calculator.
2. Select an option from the main menu by entering the corresponding number.
3. Follow the prompts to perform calculations or modify settings.
4. Results are automatically rounded according to the currently selected accuracy setting.
5. Completed calculations are automatically stored in the history system.

---

## MAIN MENU OPTIONS

1. Arithmetic Calculator
   Perform addition, subtraction, multiplication, and division.

2. Advanced Calculator
   Perform power, exponential, logarithmic, and root calculations.

3. Trigonometric Calculator
   Calculate sine, cosine, tangent, cotangent, secant, and cosecant values.

4. Show History
   Display recently performed calculations.

5. Settings
   Configure accuracy, angle units, and history options.

6. Documentation
   View complete project documentation.

7. Exit
   Safely close the application.

---

## HISTORY SYSTEM

The calculator automatically records completed calculations.

Features include:

• View recent calculations
• Clear stored history
• Configure maximum history size
• Automatic removal of the oldest entries when the history limit is reached

History is stored only while the application is running.

---

## SETTINGS

The Settings menu provides:

Accuracy Settings
• Configure the number of decimal places displayed.

Angle Unit Settings
• Degree Mode
• Radian Mode

History Settings
• View history
• Clear history
• Configure history capacity

---

## ERROR HANDLING

The calculator safely handles:

• Invalid numerical input
• Invalid menu selections
• Division by zero
• Logarithms of non-positive numbers
• Invalid root calculations
• Overflow conditions
• Undefined trigonometric functions

The application continues running after errors and allows users to correct mistakes without restarting.

---

## END OF HOW TO USE GUIDE
""")
        input()
        clear()