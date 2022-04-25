# Vehicle class
class Vehicle:
    def general_usage(self):
        print("general use: transportation")


# Car is Sub Class here and Inheriting Class Car from another Class called Vehicle
# So, you can say my car class is derived from
class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheel = 4
        self.has_roof = True

    def specific_usage(self):
        #self.general_usage()
        print("Specific Use: Commute to work, Vacation with family")


class Bike(Vehicle):
    def __init__(self):
        print("I'm motor Bike")
        self.wheel = 2
        self.has_roof = False

    def specific_usage(self):
        #self.general_usage()
        print("Specific Use: Commute to work only for single person")


c = Car()
b = Bike()

print(isinstance(c, Car))
print(isinstance(c, Bike))
print(issubclass(Car, Vehicle))
print(issubclass(Car, Bike))