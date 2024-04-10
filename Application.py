def add_task(tasks):
    num_tasks = int(input("How many tasks would you like to add: "))

    for i in range(num_tasks):
        task = input("Enter the task: ")
        tasks.append({"task":task, "done":False})
        print("Task added!")

def show_tasks(tasks):
    for index , task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def mark_tasks(tasks):
    print("-----------------------------------------------------------------\n")
    show_tasks(tasks)
    while True:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print(f"Task '{tasks[task_index]['task']}' marked as done!")
            enter_another_as_marked = input("Would you like to mark another task? yes/no: ")
            if enter_another_as_marked == "yes":
                continue
            elif enter_another_as_marked == "no":
                break
        else:
            print(f"invalid task number enter number from 1 to {len(tasks)}.")

def delete_tasks(tasks):
    print("-----------------------------------------------------------------\n")
    show_tasks(tasks)
    while True:
        task_delete_index = int(input("Enter the task number to Delete: ")) - 1 
        if 0 <= task_delete_index < len(tasks):
            tasks.remove(tasks[task_delete_index])
            print(f"Task '{tasks[task_delete_index]['task']}' removed.")
            enter_another_as_marked = input("Would you like to delete another task? yes/no: ")
            if enter_another_as_marked == "yes":
                continue
            elif enter_another_as_marked == "no":
                break
        else:
            print(f"task {task_delete_index} was not found, enter tasks from 1 to {len(tasks)}.")
            continue

def application():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            add_task(tasks)
            
        elif choice == "2":
            print("\nTasks:")
            show_tasks(tasks)
            
        elif choice == "3":
            mark_tasks(tasks)

        elif choice == "4":
            delete_tasks(tasks)

        elif choice == "5":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
application()