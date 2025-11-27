#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys


def supports_color():
   
    if os.name == "nt":
        return False
    try:
        return sys.stdout.isatty()
    except Exception:
        return False

if supports_color():
    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
else:
    RESET = GREEN = RED = CYAN = YELLOW = BOLD = ""

tasks = []

# ---- FILE HANDLING ----
FILE_NAME = "tasks.txt"

def save_tasks():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t + "\n")
    except Exception as e:
        print(RED + f"Error saving tasks: {e}" + RESET)

def load_tasks():
    tasks.clear()  # make sure we start fresh each run
    if not os.path.exists(FILE_NAME):
        return
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    tasks.append(line)
    except Exception as e:
        print(RED + f"Error loading tasks: {e}" + RESET)

# ---- MENU & UI ----
def show_menu():
    print(BOLD + CYAN + "\n====== TO-DO LIST ======" + RESET)
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Delete a task")
    print("5. Clear all tasks")
    print("6. Save tasks")
    print("7. Exit")
    print(CYAN + "========================" + RESET)

def show_tasks():
    if not tasks:
        print(RED + "No tasks yet." + RESET)
        return
    print(YELLOW + "\nYour tasks:" + RESET)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# ---- EDIT TASK ----
def edit_task():
    if not tasks:
        print(RED + "No tasks to edit." + RESET)
        return
    show_tasks()
    try:
        num = int(input("Enter task number to edit: "))
    except ValueError:
        print(RED + "Please enter a valid number." + RESET)
        return
    if 1 <= num <= len(tasks):
        new_text = input("Enter new task text: ").strip()
        if new_text:
            tasks[num - 1] = new_text
            print(GREEN + "Task updated!" + RESET)
        else:
            print(RED + "Empty text. Task not changed." + RESET)
    else:
        print(RED + "Invalid number." + RESET)

# ---- DELETE TASK ----
def delete_task():
    if not tasks:
        print(RED + "No tasks to delete." + RESET)
        return
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
    except ValueError:
        print(RED + "Please enter a valid number." + RESET)
        return
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(RED + f"Deleted: {removed}" + RESET)
    else:
        print(RED + "Invalid number." + RESET)

# ---- CLEAR ALL ----
def clear_tasks():
    confirm = input("Are you sure you want to clear everything? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.clear()
        print(RED + "All tasks cleared!" + RESET)
    else:
        print("Canceled.")

# ---- MAIN ----
load_tasks()  # load existing tasks (if any)

while True:
    show_menu()
    choice = input("Enter a number (1-7): ").strip()

    if choice == "1":
        new_task = input("Enter the task: ").strip()
        if new_task:
            tasks.append(new_task)
            print(GREEN + "Task added!" + RESET)
        else:
            print(RED + "Cannot add an empty task." + RESET)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        edit_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        clear_tasks()

    elif choice == "6":
        save_tasks()
        print(GREEN + "Tasks saved!" + RESET)

    elif choice == "7":
        save_tasks()
        print(GREEN + "Saved and exiting. Goodbye!" + RESET)
        break

    else:
        print(RED + "Invalid choice. Try again." + RESET)


# In[ ]:




