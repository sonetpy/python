"""Method Overriding
---------------------
We can provide some specific implementation of the parent class method in our child class. When the parent class method is defined in the child class with some specific implementation, then the concept is called method overriding. We may need to perform method overriding in the scenario where the different definition of a parent class method is needed in the child class.

Consider the following example to perform method overriding in python."""

print("#### Example 1")
class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d = Dog()
d.speak()

############################################
print("#### Example 2")
class Bank:
    def getroi(self):
        return 10;
class SBI(Bank):
    def getroi(self):
        return 7;
class ICICI(Bank):
    def getroi(self):
        return 8;


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b2.getroi());
print("ICICI Rate of interest:", b3.getroi());

################################################
print("#### Example3:")

class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")


sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)

########################################
print("##### Example 4")
class Person(object):
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Person Name: ", self.name)

class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display(self):
        super().display()
        print("Person ID: ", self.id)

e = Employee("surabhi", 2345)
e.display()

