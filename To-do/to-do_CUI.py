import os
def clr():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
t=[]
def ip(x):
     while True:
        try:
            y = int(input(x))
            if 1 <= y <= 5:
                return y
            print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def show_tasks():
    if not t:
        print("No tasks available.")
        return
    for i, task in enumerate(t, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. [{status}] {task['title']}")
while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    c= ip("Enter your choice: ")
    if c == 1:
        show_tasks()
        clr()
    elif c == 2:
        title = input("Enter the task : ").strip()
        if not title:
            print("Task cannot be empty.")
            clr()
            continue
        
        t.append({"title": title, "completed": False})
        print("Task added successfully.")
        clr()
    elif c == 3:
        if not t:
            print("No tasks available to mark as complete.")
            clr()
        else:
            show_tasks()
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                if 1 <= task_num <= len(t):
                    if t[task_num - 1]["completed"]:
                        print("Task is already completed.")
                        clr()
                    else:
                        t[task_num - 1]["completed"] = True
                        print("Task marked as complete.")
                        clr()
                else:
                    print("Invalid task number.")
                    clr()
            except ValueError:
                print("Invalid input. Please enter a number.")
                clr()
    elif c == 4:
        if not t:
            print("No tasks available to delete.")
            clr()
        else:
            show_tasks()
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(t):
                    removed = t.pop(task_num - 1)
                    print(f"Deleted: {removed['title']}")
                    clr()
                else:
                    print("Invalid task number.")
                    clr()
            except ValueError:
                print("Invalid input. Please enter a number.")
                clr()
    elif c == 5:
        print("Exiting the To-Do List application. Goodbye!")
        break
    