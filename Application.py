def application():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            num_tasks = int(input("How many tasks would you like to add: "))

            for i in range(num_tasks):
                task = input("Enter the task: ")
                tasks.append({"task":task, "done":False})
                print("Task added!")
        elif choice == "2":
            print("\nTasks:")
            for index , task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("invalid task number.")
        elif choice == "4":
            task_delete_index = int(input("Enter the task number to Delete: ")) - 1
            if 0 <= task_delete_index < len(tasks):
                tasks.remove(task_delete_index)
                print("Task removed.")
        elif choice == "5":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")