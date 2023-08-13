'''
Python does not support constructor overloading. If we define multiple constructors then, the interpreter will considers only the last constructor and throws an error if the sequence of the arguments doesn’t match as per the last constructor. The following example shows the same.
Example
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name
 
    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age
 
# creating first object
emma = Student('Emma')
 
# creating Second object
kelly = Student('Kelly', 13)

Output
TypeError: __init__() missing 1 required positional argument: 'age'

'''

class Student:

    def __init__(self, name, age=None):
        print("One or two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)

print(emma.name)
print(kelly.name)
print(kelly.age)
