# 4. Create a base class Person. Derive Dancer and Singer from it. 
#    Then create Performer that inherits from both Dancer and Singer 
#    and performs on stage.


class Person:
    def __init__(self,name):
        self.name = name
class Dancer(Person):
    def work(self):
        print(f"{self.name} can Dance")
class Singer(Person):
    def work(self):
        print(f"{self.name} can Sing")

class Performer(Dancer,Singer):
    def work(self):
        print(F"{self.name} can do both")

Dancer = Dancer("Dancer")
Singer = Singer("Singer")
Performer = Performer("Performer")

Singer.work()
Dancer.work()
Performer.work()
