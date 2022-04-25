# Example 1:
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id
        

class SalesPerson(Employee):
    def __init__(self, name, id, region):
        super().__init__(name, id)
        self.region = region
        
p = Person('John')
print(p.name)
e = Employee('Bob', 7468)
print(e.name, e.id)
s = SalesPerson('Jane', 4712, 'UK')
print(s.name,s.id,s.region)

#Example 2:


class Computer(object):
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd


class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model


lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)
