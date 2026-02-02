# 3. Create a base class Device. Derive Camera and Phone from it. 
#    Then create SmartGadget that inherits from both Camera and Phone 
#    and performs multitasking operations.

class Device:
    def __init__(self,name):
        self.name = name
class Camera(Device):
    def work(self):
        print(f"{self.name} can take Photo")
class Phone(Device):
    def work(self):
        print(f"{self.name} can make Calls")

class SmartGadget(Camera,Phone):
    def work(self):
        print(F"{self.name} can do both")

Camera = Camera("Camera")
Phone = Phone("Phone")
Smart = SmartGadget("SmartPhone")

Camera.work()
Phone.work()
Smart.work()
