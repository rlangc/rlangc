# Initialize an empty to-do list
todo_list = []

def show_menu():
    print("\nSimple To-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f'"{task}" added to the list!')

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f'"{removed_task}" removed from the list.')
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")