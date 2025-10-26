class Car:
    def __init__(self, brand, model):
        self.__brand = brand   # 🔒 private
        self.__model = model     # 🌐 public

    def display(self):         # 📄 show car info
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return f"{self.__brand} {self.__model}"
    
# 🚗 Base Object
car1 = Car('Kia', 'Sonet')
print(car1.display())
#car1.model='City'
#print(car1.display())
print(car1.model)

