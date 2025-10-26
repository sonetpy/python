# 🏎️ Base Class
class Car:
    # class variable — shared by all instances of Car and its subclasses
    track = 0   # keeps track of total cars created

    def __init__(self, brand, model):
        # __brand is private (encapsulation) — cannot be accessed directly outside
        self.__brand = brand       # 🔒 private variable
        self.model = model         # 🌐 public variable
        Car.track += 1             # increment class variable each time a Car (or subclass) is created

    # Public method to access private variable (__brand)
    def get_brand(self):
        return f"its brand {self.__brand} !"

    # Method to display car details
    def display(self):
        return f"You own brand {self.__brand} and model {self.model}"

    # Example of normal method (can be overridden)
    def fuel_type(self):
        return "This is petrol Car"


# ⚡ Derived Class
class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        # calling parent constructor to initialize brand and model
        super().__init__(__brand, model)
        self.battery_size = battery_size  # 🔋 new attribute specific to ElectricCar

    # overriding parent display method
    def display(self):
        # use parent display and extend it with battery info
        return f"{super().display()} battery {self.battery_size}"
    
    # overriding fuel_type to provide specialized behavior
    def fuel_type(self):
        return "its battery operated car"


# 🚗 Object of base class
car1 = Car('Kia', 'Sonet')
print(car1.display())        # ✅ prints brand and model (accesses private variable internally)
print(car1.get_brand())      # ✅ access to private data through getter method
print(car1.fuel_type())      # ✅ shows that it's a petrol car

# creating more cars — increments the class variable 'track'
Car('Tata','Safari')
Car('Hyundai','Creta')


# 🚙 Object of child class
ecar1 = ElectricCar('Tesla1', 'X', '85KwH')

# Trying to modify private brand from outside
ecar1.brand = 'BMW'      # ❌ creates a new public variable 'brand', doesn't affect __brand
ecar1.model = 'zx'       # ✅ modifies model (public variable)

# printing all details for ElectricCar
print(ecar1.display())   # ✅ shows Tesla1 (private) and updated model zx
print(ecar1.get_brand()) # ✅ still accesses encapsulated brand correctly
print(ecar1.fuel_type()) # ✅ overridden method in ElectricCar

# printing class variable — shared by all objects
print(f"total car created from car class: {Car.track}")


