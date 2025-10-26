# 🚘 Base Class
'''
🧩 Summary of Key Points
Symbol	Meaning
🔒	Private variable
🌐	Public variable
⚡	Inheritance / child class
🔋	ElectricCar-specific attribute
🔁	Method overriding
⛽	Normal instance method
📢	Static method
🧮	Class variable
'''
class Car:
    track = 0  # 🧮 shared by all cars

    def __init__(self, brand, model):
        self.__brand = brand   # 🔒 private
        self.model = model     # 🌐 public
        Car.track += 1         # ➕ count new car

    def get_brand(self):       # 🎯 getter for private brand
        return f"Brand: {self.__brand}"

    def display(self):         # 📄 show car info
        return f"{self.__brand} {self.model}"

    def fuel_type(self):       # ⛽ normal method
        return "Petrol car"

    @staticmethod
    def general_description(): # 📢 static info
        return "Cars are means of transport"


# ⚡ Child Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery  # 🔋 unique to ElectricCar

    def display(self):          # 🔁 override
        return f"{super().display()} | Battery: {self.battery}"

    def fuel_type(self):        # ⚙️ override
        return "Battery operated car"


# 🚗 Base Object
car1 = Car('Kia', 'Sonet')
print(car1.display())
print(car1.get_brand())
print(car1.fuel_type())

# ➕ Create more cars
Car('Tata', 'Safari')
Car('Hyundai', 'Creta')
Car('Mahindra', 'XUV')
print(Car.general_description())

# 🚙 ElectricCar Object
ecar1 = ElectricCar('Tesla', 'X', '85kWh')
ecar1.brand = 'BMW'   # ❌ new public var (doesn’t touch private one)
ecar1.model = 'ZX'    # ✅ updates public var

print(ecar1.display())
print(ecar1.get_brand())
print(ecar1.fuel_type())

# 📊 Total Cars Created
print(f"Total Cars: {Car.track}")