'''
🧩 Your next 2 tasks

Task 3:
Create a class Person with:
__init__(self, name)
greet(self) → returns "Hello, my name is <name>"
Then make a subclass Employee that:
ues super().__init__(name)
adds a new attribute role
overrides greet() to return parent’s greeting + " and I work as a <role>."

Task 4:
Create a subclass Manager that inherits from Employee,

adds an attribute team_size

overrides greet() to call super().greet() and append " I manage a team of <team_size> people."

Once you’ve coded both and printed outputs for each (Person, Employee, Manager), paste them here.
I’ll check your use of super() — that’s where OOP starts to really connect.
'''
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}"
    
class Employee(Person):
    def __init__(self,name,role):
        super().__init__(name)
        self.role = role

    def greet(self):
        return f"{super().greet()} and I work as a {self.role}."
        
class Manager(Employee):
    def __init__(self, name, role, team_size):
        super().__init__(name, role)        # call Employee's constructor
        self.team_size = team_size
    def greet(self):
        return f"{super().greet()} I manage a team of {self.team_size} people."
    
p = Person("Amit")
print(p.greet())

e = Employee("Ravi", "Engineer")
print(e.greet())

m = Manager("Neha", "Project Manager", 8)
print(m.greet())
