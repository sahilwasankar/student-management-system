# Main program for the Student Management System

from student import Student
from manager import StudentManager

# Displays the main menu with all available options
def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ====== ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("=======================================")

# Creates an instance of StudentManager to handle student data
manager = StudentManager()

# Get and validate student input
def get_valid_student_data():

    while True:
     try:
       sid =  input("ID: ").strip()
       break
       
     except ValueError:
        print("Input the valid integer only!")    

    while True:
        name = input("Name: ").strip()
        if name :
            break
        print("The name input should not be empty")
                     
    while True:
     try :
         age = int(input("Age: "))
         if age > 0:             
            break
         print("Age must be positive")

     except ValueError:
         print("Age must be a number")


    while True:
        course = input("Course: ")
        if course:
            break
        print("Course should not be empty")


    return sid,name,age,course


# Main program loop
while True:
    show_menu()
    choice = input("Enter choice: ")

    # Add a new student
    if choice == "1":
        sid, name, age, course = get_valid_student_data()
        student = Student(sid, name, age, course)
        manager.add_student(student) 
        
    # View all students    
    elif choice == "2":
        manager.view_students()

    # Search student by ID
    elif choice == "3":
         sid = input("Enter Student ID to search: ")
         manager.search_student(sid)

    # Delete student by ID
    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        manager.delete_student(sid)    

    # Exit program
    elif choice == "5":
        print("Goodbye 👋")
        break

    # Invalid menu choice
    else:
        print("Please select a valid menu option")



    



    
    


