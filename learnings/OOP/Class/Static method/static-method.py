class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y


print(MathUtils.add(10, 20))
print(MathUtils.subtract(30, 10))


# The `add()` and `subtract()` methods are both static methods. They can be called without creating an object of the `MathUtils` class. For example:

print(MathUtils.add(10, 20))
# 30

print(MathUtils.subtract(30, 10))
# 20

# As you can see, we were able to call the `add()` and `subtract()` methods without creating an object of the `MathUtils` class. This is because they are static methods.

# In Python, static methods are defined using the `@staticmethod` decorator. The `@staticmethod` decorator tells Python that the method is a static method, and that it does not need to be called on an object of the class.

#Static methods are often used to perform utility functions that do not depend on any particular instance of a class. For example, the `MathUtils` class in the example above contains two static methods for performing mathematical operations. These methods can be used by any class, without the need to create an object of the `MathUtils` class.

#Here are some other examples of when you might use static methods in Python:
"""
* To provide a common implementation for a method that is used by multiple classes.
* To provide a way to access a shared resource, such as a database or file.
* To implement a mathematical algorithm or other complex calculation.
"""

#Static methods can be a very powerful tool when used correctly. They can help to make your code more modular and reusable.