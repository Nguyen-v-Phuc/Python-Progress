def menu():
    print("\n--- STUDENT SYSTEM ---")
    print("1. Add student")
    print("2. View students")
    print("3. Update student_score")
    print("4. Delete student")
    print("5. Exit")

def add_students():
    student_name = input("Enter student name: ")
    student_score = int(input("Enter student score: "))

    with open("CRUD.txt", 'a') as file:
        file.write(f"\n{student_name}, {student_score}")

def view_students():
    with open("CRUD.txt", "r") as file:
        content = file.read()
    print(content)

def update_students_score():
    name_to_update = input("Enter name to update: ")

    updated_lines = []

    with open("CRUD.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")

            if name == name_to_update:
                new_score = input("New score: ")
                updated_lines.append(f"{name}, {new_score}\n")
            else:
                updated_lines.append(line)

    with open("CRUD.txt", "w") as file:
        file.writelines(updated_lines)

def delete_student():
    target = input("Name to delete: ")

    with open("CRUD.txt", "r") as file:
        lines = file.readlines()
    with open("CRUD.txt", "w") as file:
        for line in lines:
            if target not in line:
                file.write(line)

def exit():
    return 0

def main():
    while True:
        menu()
        choice = int(input("Choose: "))
        if choice == 1:
            add_students()
        elif choice == 2:
            view_students()
        elif choice == 3:
            update_students_score()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()