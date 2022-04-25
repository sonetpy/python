def outer(name):
    # this is the enclosing function

    def inner():
        # this is the enclosed function

        # the inner function accessing the outer function's variable 'name'
        print(name)

    inner()

# call the enclosing function
outer('TechVidvan')

"""
Let’s break this code down.
When the outer function gets called, the variable ‘name’ gets the value ‘TechVidvan’. The inner function can access the value of this variable. When the inner function gets called, ‘Techvidvan’ gets printed. This is how scope works in nested functions.
The bottom line is (and it’s worth repeating) – “Enclosed functions can access the variables of enclosing functions.”
Keeping this in mind, let’s move on to Python closures.

Python Closures
----------------------
In the example above, we have called the inner function inside the outer function. The inner function becomes a closure when we return the inner function instead of calling it.

So we have a closure in Python if-

We have a nested function, i.e. function within a function
The nested function refers to a variable of the outer function
The enclosing function returns the enclosed function
"""


def outer(name):
    # this is the enclosing function

    def inner():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'name'
        print(name)

    return inner


# call the enclosing function
myFunction = outer('TechVidvan')
myFunction()
