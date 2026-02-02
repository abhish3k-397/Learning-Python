# class Car:
#     company = "None"
#     model = "None"
#     year = 0
#     speed = 0

# my_car = Car()
# print(my_car)
#print(my_car.company)

# class Car:
#     def __init__(company, speed):
#         company = company
#         speed = speed


class Car:
    def __init__(self, company, speed):
        self.company = company
        self.speed = speed
    def accel(self):
        self.speed += 1
    def display(self):
        print(f"Company: {self.company}, Speed: {self.speed}")
car1 = Car("Tata",67)
car1.display()
car2 = Car("Toyota", 789)
car2.accel()
car2.display()
str1 = input("Input Your Car Brand: ")
int1 = input("Input your Car Speed: ")
car3 = Car(str1,int1)
car3.display()