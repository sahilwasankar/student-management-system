class Student:

   def __init__(self, student_id, name, age, course):
     self.student_id = student_id
     self.name = name
     self.age = age
     self.course = course

   def to_csv_row(self):
     return [self.student_id, self.name, self.age, self.course]
    
    


