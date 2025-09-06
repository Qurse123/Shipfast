# Personal Task Manager - Learning Arrays in Python
import array 

def display_menu():
    print("\n=== Personal Task Manager ===")
    print("1. Add a new task: ")
    print("2. View all tasks: ")
    print("3. Mark task as complete: ")
    print("4. Remove a task: ")
    print("5. Quit: ")

def add_task(tasks):
    add=input("Add a task")
    tasks.append({"task": add, "completed": False})
    print("Task added!")
    return

def view_tasks(tasks):
    if len(tasks) == 0:
            print("No tasks added yet!")
            return
    for index, task_dict in enumerate(tasks): ## index goes first then use the variable add which is the inputed user task them enumurate tasks you get (index, add) == (0, walk dog) (1, do dishes)
        if task_dict["completed"] == True:
            print(f"{index + 1}. {task_dict["task"]} ✅")
        else:
            print(f"{index + 1}. {task_dict["task"]}")  ## (index + 1). walk dog eg first added task == (0+1) = 1. walk dog
    return 

def mark_complete(tasks):
    complete = input("what tasks did you comeplete, input number?")

    for index, task_dict in enumerate(tasks):
        if int(complete) == index + 1:
            task_dict["completed"] = True
            print(f"{complete}. {task_dict["task"]} ✅")
        

def remove_task(tasks):
    for index, task_dict in enumerate(tasks):
        print(f"{index + 1}. {task_dict["task"]}")

    finished = input("which numbered tasks to delete?")
    
    for index, task_dict in enumerate(tasks):
        if int(finished) == index + 1:
            tasks.pop(index)
            print("This task has been deleted")
            return

def main():
    tasks = []  # Our main array to store an array of dictionaries
    
    print("Welcome to your Personal Task Manager!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Thanks for using Task Manager! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
