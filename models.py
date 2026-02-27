class Student:
    def __init__(self, student_id, name, age, gender, course, marks):
        self.id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"{self.id} | {self.name} | {self.age} | {self.gender} | {self.course} | {self.marks}"
