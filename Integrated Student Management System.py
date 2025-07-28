import os

STUDENT_FILE = "students.txt"

def load_students():
    students = {}
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                if line.strip():
                    student_id, name, grade = line.strip().split(",")
                    students[student_id] = {"name": name, "grade": grade}
    return students

def save_students(students):
    with open(STUDENT_FILE, "w") as file:
        for student_id, data in students.items():
            file.write(f"{student_id},{data['name']},{data['grade']}\n")

def add_student(students):
    try:
        student_id = input("Enter student ID: ").strip()
        if student_id in students:
            print("Error: Student ID already exists!")
            return
            
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")
            
        grade = input("Enter student grade: ").strip()
        if not grade:
            raise ValueError("Grade cannot be empty")
            
        students[student_id] = {"name": name, "grade": grade}
        save_students(students)
        print("Student added successfully!")
        
    except ValueError as e:
        print(f"Error: {e}")

def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    if student_id in students:
        print(f"\nStudent found:\nID: {student_id}\nName: {students[student_id]['name']}\nGrade: {students[student_id]['grade']}")
    else:
        print("Student not found!")

def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    if student_id in students:
        try:
            print(f"\nCurrent information:\nName: {students[student_id]['name']}\nGrade: {students[student_id]['grade']}")
            name = input("Enter new name (leave blank to keep current): ").strip()
            if name:
                students[student_id]['name'] = name
            grade = input("Enter new grade (leave blank to keep current): ").strip()
            if grade:
                students[student_id]['grade'] = grade
            save_students(students)
            print("Student updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Student not found!")

def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def display_all_students(students):
    if not students:
        print("No students in the system!")
        return
    print("\nAll Students:")
    for student_id, data in students.items():
        print(f"ID: {student_id}, Name: {data['name']}, Grade: {data['grade']}")

def main_menu():
    students = load_students()
    while True:
        print("\nStudent Management System\n1. Add Student\n2. Search Student\n3. Update Student\n4. Delete Student\n5. Display All Students\n6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            display_all_students(students)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main_menu()