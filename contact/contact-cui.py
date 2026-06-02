import os
c=[]
def clr():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def add():
    name = input("Enter name: ")
    try:
        phone = int(input("Enter phone number: "))
    except ValueError:
        print("Invalid phone number.")
        clr()
        return
    email = input("Enter email: ")
    address = input("Enter address: ")
    for contact in c:
        if contact['phone'] == phone:
            print("Contact with this phone number already exists.")
            print(contact)
            clr()
            return
    c.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print("Contact added.")
    clr()

def view():
    if not c:
        print("No contacts found.")
    else:
        for i, contact in enumerate(c, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    clr()

def search():

    q = input("Enter name or phone number to search: ")
    
    found = [contact for contact in c if q.lower() in contact['name'].lower() or q in str(contact['phone'])]
    if found:
        for i, contact in enumerate(found, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("Contact not found.")
    clr()

def update ():
    view()
    try:
        idx = int(input("Enter contact number to update: ")) - 1
        if 0 <= idx < len(c):
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address= input("Enter new address (leave blank to keep current): ")
            if name:
                c[idx]['name'] = name
            if phone:
                c[idx]['phone'] = int(phone)
            if email:
                c[idx]['email'] = email
            if address:
                c[idx]['address'] = address
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Numbers only.")
    clr()

def delete():
    view()
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if 0 <= idx < len(c):
            del c[idx]
            print("Contact deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Numbers only.")
    clr()
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. How to Use/Documentation")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            search()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            print(''' 📇 Contact Management System (CLI)

A simple command-line based Contact Management System built using Python.
This application allows users to store and manage contact details efficiently.

---

## 🚀 Features

- Add new contacts (Name, Phone, Email, Address)
- View all saved contacts
- Search contacts by name or phone number
- Update existing contact details
- Delete contacts
- Menu-driven interface
- In-app documentation

---

## 🛠️ How to Run

1. Ensure Python 3 is installed

2. Save the file as:
   contact_manager.py

3. Open terminal / command prompt

4. Navigate to the project folder

5. Run the program:
   python contact_manager.py

---

## 📖 How to Use

### 1. Add Contact
- Enter name, phone number, email, and address
- Contact will be saved in memory

### 2. View Contacts
- Displays all contacts with full details

### 3. Search Contact
- Search using:
  - Name (case-insensitive)
  - Phone number

### 4. Update Contact
- Select contact using its number
- Leave fields blank to keep existing values

### 5. Delete Contact
- Select contact using its number
- Contact will be removed

### 6. Documentation
- Displays usage instructions within the program

### 7. Exit
- Closes the application

---

## 🧠 Data Structure

- Contacts are stored as a list of dictionaries:
  
  Example:
  {
    "name": "John",
    "phone": 1234567890,
    "email": "john@email.com",
    "address": "City"
  }

---

## ⚠️ Limitations

- Data is NOT saved permanently
- Phone numbers must be numeric
- No input validation for email format

---

## 🔮 Future Improvements

- Save contacts to file (JSON/CSV)
- Add validation (email, phone)
- Prevent duplicate entries
- Add unique ID system
- GUI version

---

## 👨‍💻 Developer Details

Name: Your Name  
Project: Contact Management System  
Language: Python  

Concepts Used:
- Lists & Dictionaries
- Functions
- Loops & Conditionals
- Exception Handling
- CLI-based UI

---

## 💬 Final Note

This project demonstrates CRUD operations and basic data handling
in a command-line environment.

Simple, functional, and expandable.''')
        elif choice == 7:
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Choose 1-7.")
    except ValueError:
        print("Invalid input. Numbers only.")