# 1. Create a base class University. Derive Student and Teacher from it. 
#    Then create TeachingAssistant that inherits from both Student and Teacher 
#    and implements methods for studying, teaching, and assisting.

class University:
    def __init__(self,name):
        self.name = name
class Student(University):
    def studying(self):
        print(f"{self.name} is Studying")
class Teacher(University):
    def teaching(self):
        print(f"{self.name} is Teaching")

class TeachingAssistant(Student,Teacher):
    def assisting(self):
        print(F"{self.name} is Assisting in Teaching")

Arjun = TeachingAssistant("Arjun")
Arjun.assisting()

Arjun.teaching()
Arjun.studying()

Arun = Student("Arun")

Arun.studying()
