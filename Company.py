# 5. Create a base class Company. Derive Programmer and Tester from it. 
#    Then create SoftwareEngineer that inherits from both Programmer and Tester 
#    and handles complete software development.

class Company:
    def __init__(self,name):
        self.name = name
class Programmer(Company):
    def work(self):
        print(f"{self.name} can Code")
class Tester(Company):
    def work(self):
        print(f"{self.name} can Test")

class SoftwareEngineer(Programmer,Tester):
    def work(self):
        print(F"{self.name} can do both")

Programmer = Programmer("Programmer")
Tester = Tester("Tester")
SoftwareEngineer = SoftwareEngineer("SoftwareEngineer")

Tester.work()
Programmer.work()
SoftwareEngineer.work()
