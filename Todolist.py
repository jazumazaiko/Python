print("Welcome to your To-Do List!");

task = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        new_task = input("Enter the task you want to add: ")
        task.append(new_task)
        print(f"Task '{new_task}' added to the list.")
    
    elif choice == '2':
        if not task:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
    
    elif choice == '3':
        if not task:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
            try:
                remove_idx = int(input("Enter the number of the task you want to remove: "))
                if 1 <= remove_idx <= len(task):
                    removed_task = task.pop(remove_idx - 1)
                    print(f"Task '{removed_task}' removed from the list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '4':
        print("Exiting the To-Do List. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")