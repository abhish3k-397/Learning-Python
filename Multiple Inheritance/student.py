class School:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Name of School: {self.name}")

class Student(School):
    delf __init__(self,name,grade)