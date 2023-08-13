# https://www.programiz.com/article/python-self-why

# Class and Object
class Employee:
    company = "yahoo"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_email(self):  # Self is instance method here
        return f'{self.fname}.{self.lname}@{Employee.company}.com'


emp1 = Employee('kumar', 'abhinav')
print(emp1.get_email())


# Just like instance method takes first parameter as self so class Method takes Class as first Parameter in the form of cls.
# Class Method

""""
If we want multiple and independent "constructors", we can use class methods. They are usually called factory methods.
It does not invoke the default constructor __init__.In the above example, we split the string based on the "-" operator. 
We first create a class method as a constructor that takes the string and split it based on the specified operator.
 For this purpose, we use a split() function, which takes the separator as a parameter. 
This alternative constructor approach is useful when we have to deal with files containing string data separated by a separator.
"""
class Employee:
    company = "yahoo"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_email(self):  # Self is instance method here
        return f'{self.fname}.{self.lname}@{Employee.company}.com'

    @classmethod
    def change_company(cls, new_name):  # This is a class Method
        cls.company = new_name


# CLS will take the value Employee
Employee.change_company("google")
emp1 = Employee('kumar', 'abhinav')
print(emp1.get_email())