import os
import secrets
def clr():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
s = 3  
while True:
    print("\nWelcome to Pass-Gen!")
    print("1. Generate a password")
    print("2. Settings")
    print("3. How to use")
    print("4. Exit")
    try:
        c = int(input("Enter your choice: "))
        if c not in [1, 2, 3, 4]:
            print("Choose 1-4.")
            continue        
    except ValueError:
        print("Invalid input. Numbers only.")
        continue
    if c == 1:
        while True:
            try:
                length = int(input("Enter password length: "))
                if length > 0:
                    break
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Numbers only.")
        if s == 1:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif s == 2:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(secrets.choice(chars) for _ in range(length))
        print("\nGenerated password:", password)
        clr()
    elif c == 2:
        while True:
            print("\nSettings:")
            print("Choose password complexity:")
            print(f"Current setting: {s} \n")
            print("1. Only letters")
            print("2. Letters + numbers")
            print("3. Letters + numbers + symbols")
            print("4. Back")
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 3:
                    s = choice
                    print("Settings updated.")
                    clr()
                elif choice == 4:
                    break
                else:
                    print("Choose 1-4.")
            except ValueError:
                print("Numbers only.")
    elif c == 3:
        print('''=========== PASS-GEN HELP ===========

Welcome to Pass-Gen, a simple password generator.

MENU OPTIONS:
1. Generate a password
   - Enter desired length
   - Password will be generated instantly

2. Settings
   - Choose password complexity:
     1 → Letters only
     2 → Letters + Numbers
     3 → Letters + Symbols

3. How to use
   - Displays this help file

4. Exit
   - Closes the program

------------------------------------

NOTES:
- Longer passwords = stronger passwords
- Complexity increases security
- Generated passwords are random and not stored

------------------------------------

TIP:
If you're still using "123456",
this program is already doing more work than you are.

====================================''')
        clr()
    elif c == 4:
        print("Exiting Pass-Gen. Goodbye!")
        break