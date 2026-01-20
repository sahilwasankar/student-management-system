import os
import csv
from student import Student


class StudentManager:
    def __init__(self, filename="data/students.csv"):
        self.filename = filename
        self.students = []

        # Auto create file if missing
        if not os.path.exists(self.filename):
            with open(self.filename,"w", newline="") as file:  
                pass
            
            
        self.load_students()

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
            pass  # File will be created on first save

    def save_students(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow(student.to_csv_row())

    def student_exists(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return True
        return False 
    
    def add_student(self, student):
        if self.student_exists(student.student_id):
            print("Student ID already exists. Use a unique ID.")
            return
        
        self.students.append(student)
        self.save_students()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(
              f" ID: {student.student_id}, Name: {student.name}, Age: { student.age}, Course: {student.course}"
            ) 


    def search_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(
                f" ID: {student.student_id}\n Name: {student.name}\n Age: { student.age}\n Course: {student.course}"

            )
                return
        print("Student not found.")    



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
                  print("Student deleted successfully")
                else:
                    print("Delete operation cancelled.")  

                return
        print("Student ID not found.")

        
