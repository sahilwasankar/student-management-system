import csv
from student import Student

class StudentManager:
    def __init__(self, filename="data/students.csv"):
        self.filename = filename

    def add_student(self, student):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(student.to_csv_row())

    def view_students(self):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
