'''Task 1:
Create a class Vehicle with:
__init__(self, brand)
method start() → returns "Vehicle is starting"
Then make a subclass Car that:
inherits from Vehicle
overrides start() to return "Car engine is roaring"

Task 2:
Create another subclass Bike that:
also inherits from Vehicle
does not override start()
Then test both Car and Bike to see how inheritance behaves.
'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Vehicle is starting"

class Car(Vehicle):
    def start(self):
        return "Car engine is roaring"

car = Car("Toyota")
print(car.start())  # Output: Car engine is roaring

vehicle = Vehicle("Honda")
print(vehicle.start())  # Output: Vehicle is starting

class Bike(Vehicle):
    def start(self):
        return super().start()

bike = Bike("Yamaha")
print(bike.start())  # Output: Vehicle is starting
