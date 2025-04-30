# creating  a text based todo list

def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")
    return
# allows for user to add tasks
def add_task(tasks):
    task =input("Enter task description:")
    tasks.append(task)
    print("Task added successfully!")
    
# allows them to view the tasks added
def view_task(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done")
        return
    
    view_task(tasks) #Displays tasks with indices
    index = int(input("Enter task index to mark done:")) -1

    if 0 <= index < len(tasks):
        removed_tasks = tasks.pop(index)
        print(f"task '{removed_tasks}' markde as done and removed")
    else:
        print("Invalid task index")

def main()
    tasks = [] # initialize an empty list to  store tasks

    while True:
        display_menu()

        choice = input("Enter your choice:")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("GoodBye")
            break
        else:
            print("Invalid choice.")


if __name__=="__main__":
    main()

def save_tasks(tasks)
    with open("tasks.txt", "w") as f:
              for task in tasks:
                f.write(task + '\n')

def load_task():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return[]


