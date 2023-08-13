"""
Python allows us to define a constructor with default values. The default value will be used if we do not pass arguments to the constructor at the time of object creation.
The following example shows how to use the default values with the constructor.
"""
class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()
