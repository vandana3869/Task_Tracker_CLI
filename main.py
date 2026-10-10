from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add task\n2. Update task\n3. List tasks\n4. Delete task\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Task description: ").strip()
            if description:
                manager.add_task(description)
            else:
                print("Description cannot be empty.")

        elif choice == "2":
            task_id = int(input("Task ID: ").strip())
            description = input("New description (Enter to keep current): ").strip()
            status = input("New status (todo, in-progress, done; Enter to keep): ").strip()
            try:
                manager.update_task(
                    task_id,
                    description=description or None,
                    status=status or None,
                )
            except ValueError as error:
                print(error)
        elif choice == "3":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.created_at}, Updated At: {task.update_at}")

        elif choice == "4":
            task_id = int(input("Task ID: ").strip())
            task = manager.get_task(task_id)
            if task:
                manager.remove_task(task_id)
            else:
                print(f"Task with ID {task_id} not found.")

        elif choice == "5":
            break

        else:
            print("Choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()