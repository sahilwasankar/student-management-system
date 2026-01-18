# csv is a built-in Python module
# It helps you read from and write to CSV files
# CSV = Comma Separated Values
# Student Management System - Local Git Setup

from student import Student
from manager import StudentManager

def show_menu():
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

manager = StudentManager()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")

        student = Student(sid, name, age, course)
        manager.add_student(student)
        print("Student added!")

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
