"""
The isinstance (obj, class) method
The isinstance() method is used to check the relationship between the objects and classes.
It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.
"""

class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(isinstance(d,Derived))

"""
The issubclass(sub,sup) method
The issubclass(sub, sup) method is used to check the relationships between the specified classes. 
It returns true if the first class is the subclass of the second class, and false otherwise.
"""
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))