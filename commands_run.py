import sys

# File where tasks will be stored
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the tasks file."""
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        pass  # If file doesn't exist, return an empty task list
    return tasks

def save_tasks(tasks):
    """Save tasks to the tasks file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(description):
    """Add a task with the given description."""
    tasks = load_tasks()
    tasks.append(description)
    save_tasks(tasks)
    print(f'Task added: "{description}"')

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task(task_number):
    """Mark a task as completed and remove it from the list."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task completed: "{completed_task}"')
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete task from list."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task deleted: "{deleted_task}"')
    else:
        print("Invalid task number.")

def main():
    """Main function to execute actions."""
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py add <task description>")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        list_tasks()

    elif command == "complete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python task_manager.py complete <task number>")
        else:
            complete_task(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python task_manager.py delete <task number>")
        else:
            delete_task(int(sys.argv[2]))

    else:
        print("You have entered an unknown command. Available commands are as follows: add, list, complete, delete")

if __name__ == "__main__":
    main()
