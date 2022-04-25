"""
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
In the above program, we define two methods i.e sing() and dance().
These are called instance methods because they are called on an instance object i.e blu.
"""
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())