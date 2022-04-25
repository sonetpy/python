"""
https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-68/

Today we are going to learn the concept of abstract class and abstract method. Let us begin our tutorial with some definitions. First, we will define the abstract class:
“An abstract class is a class that holds an abstract method.”
And
“An abstract method is a method defined inside an abstract class.”
The definition may appear too simple, but the abstract method holds all the cards because it is necessary for all classes derived by the abstract class to have the same method even though their functionality and code may differ.
However, the name of the method should be the same as the abstract method. The abstract method inside the abstract class could even be empty because we can not implement it anywhere.
It is just so that all the other classes define a method by the same name.

It is important to remember that we can not make an object for an abstract class.
Following is the syntax for defining an abstract method in an abstract class in Python:

from abc import ABC, abstractmethod
Class MyClass(ABC):
      @abstractmethod
      def mymethod(self):
            #empty body
            pass

To implement an abstract class, we have to import the abc module by using an import statement. Along with it, we have to import the abstract method too. If we are using a Python version older than 3.4, then we have to write:

from abc import ABCMeta, abstractmethod


Moreover, we have to pass ABCMeta into the class, which we are defining as abstract.
Although if our version is newer, then we can import by the statement:

From <https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-68/>

from abc import ABC, abstractmethod

And we have to pass ABC to the class we are defining as abstract.
To make a method specifically abstract in a class, we use the abstract method decorator denoted as @absttractmethod, which is defined in the abc module.
To understand the abstract class and method better, let us take an example. Suppose we have a few classes related to different items in a bookstore.
Now our classes are books, stationery, and magazines. All these products are dealt with separately, so all of these classes must have a method named sale that could return the amount achieved by selling these items.
So to ensure that each of these classes has a sale method, we will make an abstract class named bookstore with an abstract method Sale and will derive all the other three classes from it.
Until we have made a method Sale in each of the derived classes, we would not be able to make its object, or the compiler will report an error.
Important points about abstract class in Python:
1. Abstract methods are defined in the abstract class. They mostly do not have the body, but it is possible to implement abstract methods in the abstract class.
Any subclass deriving from such an abstract class still needs to provide an implementation for that abstract method.
2. An abstract class can have both abstract methods as well as concrete methods.
3. The abstract class works as a template for other classes.
4. Using the abstract class, we can define a structure without properly implementing every method.
5. It is not possible to create objects of an abstract class because Abstract class cannot be instantiated.
6. An error will occur if the abstract method has not been implemented in the derived class.

"""

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

