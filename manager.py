import os
import csv
from student import Student

# Handles all the student related operations using CSV storage
class StudentManager:
    def __init__(self, filename="data/students.csv"):
        self.filename = filename
        self.students = []

        # Auto create file if missing
        if not os.path.exists(self.filename):
            with open(self.filename,"w", newline="") as file:  
                pass
            
            
        self.load_students()
    # Loads existing student records into the self.students list
    def load_students(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    student = Student(
                        student_id=row[0],
                        name=row[1],
                        age=int(row[2]),
                        course=row[3]
                    )
                    self.students.append(student)
        except FileNotFoundError:
            pass  

    # Writes student records to the CSV file in row format
    def save_students(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow(student.to_csv_row())

    # Checks Whether the student ID already exists
    def student_exists(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return True
        return False 
    
    # Adds a new student to the system during program execution
    def add_student(self, student):
        if self.student_exists(student.student_id):
            print("Student ID already exists. Use a unique ID.")
            return
        
        self.students.append(student)
        self.save_students()
        print("Student added successfully ✅")

    # Displays all student records present in the CSV file
    def view_students(self):
        if not self.students:
            print("No students found ❌")
            return
        for student in self.students:
            print(
              f" ID: {student.student_id}, Name: {student.name}, Age: { student.age}, Course: {student.course}"
            ) 

    # Searches for a student by student ID
    def search_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(
                f" ID: {student.student_id}\n Name: {student.name}\n Age: { student.age}\n Course: {student.course}"

            )
                return
        print("Student not found ❌")    


    # Deletes a student record using the student ID
    def delete_student(self,student_id):
        for student in self.students:
            if(student.student_id == student_id):
                print("\nStudent Found:")
                print(
                f" ID: {student.student_id}\n Name: {student.name}\n Age: { student.age}\n Course: {student.course}"
            )
                confirm = input("Are you sure you want to delete this student? (yes/no): ").lower()

                if confirm == "yes":

                  self.students.remove(student)
                  self.save_students()
                  print("Student deleted successfully 🗑️")
                else:
                    print("Delete operation cancelled.")  

                return
        print("Student ID not found ❌")

        
