# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def display(self):
#         print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")

# n = input("How many students are in class?: ")
# for i in range(n+1):
        

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")


n = int(input("How many students are in class?: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    name = input("Name: ")
    rollno = int(input("Roll No: "))
    marks = float(input("Marks: "))

    s = Student(name, rollno, marks)
    s.display()
