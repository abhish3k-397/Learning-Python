# 8. Create a base class School. Derive SportsStudent and MusicStudent from it. 
#    Then create AllRounder that inherits from both SportsStudent and MusicStudent 
#    and performs multiple talents.

class School:
    def __init__(self,name):
        self.name = name
class SportsStudent(School):
    def work(self):
        print(f"{self.name} can Code")
class MusicStudent(School):
    def work(self):
        print(f"{self.name} can Test")

class AllRounder(SportsStudent,MusicStudent):
    def work(self):
        print(F"{self.name} can do both")

SportsStudent = SportsStudent("SportsStudent")
MusicStudent = MusicStudent("MusicStudent")
AllRounder = AllRounder("AllRounder")

MusicStudent.work()
SportsStudent.work()
AllRounder.work()
