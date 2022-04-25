"""
Data abstraction in python
Abstraction is an important aspect of object-oriented programming.
In python, we can also perform data hiding by adding the double underscore (___) as a prefix to the attribute which is to be hidden.
After this, the attribute will not be visible outside of the class through the object.
"""
class Employee:
    __count = 0;
    #count = 0
    def __init__(self):
        #Employee.count = Employee.count+1
        Employee.__count = Employee.__count+1

    def display(self):
        print("The number of employees",Employee.__count) # Employee.count
emp = Employee()
emp2 = Employee()
try:
    #print(emp.count)
    print(emp.__count)

finally:
    emp.display()

