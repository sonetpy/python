# By calling methods
class Person():
    def set_details(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am Person ', self.name)
    def greet(self):
        if self.age < 80:
            print('hello, how are you doing?')
        else:
            print("Hello, how do you do ? ")
        self.display()

p1 = Person()
p2 = Person()

p1.set_details('Bob', 29)
p2.set_details('Marley', 90)

p1.greet()
p2.greet()

print("Using __init__ method or dunder method or initilization method")
# By calling __init__ (dunder method)
# https://www.udemy.com/course/object-oriented-python-programming/learn/lecture/18241922#notes
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def display(self):
        print('I am Person ', self.name)
    def greet(self):
        if self.age < 80:
            print('hello, how are you doing?')
        else:
            print("Hello, how do you do ? ")
        self.display()

p1 = Person('Bob', 29)
p2 = Person('Marley', 90)
p1.display()
p1.greet()
p2.display()
p2.greet()
