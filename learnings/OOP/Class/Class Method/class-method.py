#Class Methods
#In Object-oriented programming, Inside a Class, we can define the following three types of methods.
    #• Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.

    #• Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.

    #• Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.

class Student():
    # class variable
    school="Sadharan"

    # constructor
    def __init__(self,name,age):
        # instance variable
        self.name=name
        self.age=age

    # instance method
    def details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSchool :{Student.school}")

    # class method
    @classmethod
    def modify_school_name(cls,new_name):
        cls.school=new_name

stud=Student("Abhinav",23)
stud.details()

#Modify instance variable
stud.name="aamir"
stud.age=23
stud.details()

# call class method
Student.modify_school_name('killer school')
stud.details()