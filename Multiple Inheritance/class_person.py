class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    def show(self):
        print(f"Name: {self.name} , Roll No: {self.roll_no}")

bee 