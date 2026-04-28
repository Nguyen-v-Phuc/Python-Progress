tasks = []
print("---Welcome to your To-do list program---")

def add_task():
    number = input("How many tasks do you want to add? ")

    for i in range(int(number)):
        task = input("Enter your task: ")
        tasks.append(task)

    main()

def view():
    print("Your tasks are: ")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

    main()

def complete_task():
    done = int(input("Which tasks do you want mark to complete? "))

    print(f"Task: {tasks[done - 1]} is complete")

    main()

def delete_task():
    index = int(input("Enter a task to delete: "))

    tasks.pop(index - 1)
    print("Task deleted successfully")
    main()

def exit_program():
    print("Exited successfully")
    return 0

def main():
    print("What are you going to do?")
    print("1. Add task")
    print("2. View task")
    print("3. complete_task")
    print("4. Delete task")
    print("5. Exit")
    choose = input("Enter your choice: ")

    if choose == "1":
        add_task()
    elif choose == "2":
        view()
    elif choose == "3":
        complete_task()

    elif choose == "4":
        delete_task()
    elif choose == "5":
        exit_program()

if __name__ == "__main__":
        main()