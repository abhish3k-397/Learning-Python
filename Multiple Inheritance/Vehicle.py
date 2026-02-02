# 2. Create a base class Vehicle. Derive Car and Boat from it. 
#    Then create AmphibiousVehicle that inherits from both Car and Boat 
#    and shows land and water transportation.


class Vehicle:
    def __init__(self,name):
        self.name = name
class Car(Vehicle):
    def land(self):
        print(f"{self.name} runs on Land")
class Boat(Vehicle):
    def water(self):
        print(f"{self.name} runs on Water")

class AmphibiousVehicle(Car,Boat):
    def amphi(self):
        print(F"{self.name} run on both land and water")

Car = Car("Car")
Boat = Boat("Boat")
Car.land()
Boat.water()
Seaplane = AmphibiousVehicle("SeaPlane")
Seaplane.amphi()