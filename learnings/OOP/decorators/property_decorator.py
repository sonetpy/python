class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + ' ' + self.lname

    # generate email using fname and lname
    def email(self):
        return f'{self.fname}.{self.lname}@indian.com'


# Let's now create a few objects and call the function email() and doing so try a few things,
# student s1
s1 = Student('tony', 'stark')
print('Fullname of s1 is: ', s1.fullname)
print('And email is: ', s1.email())

# Now updating the s1 object's first name
s1.fname = 'steve'
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

"""
Now coming to the output, we can see that for a student when the first name is changed then email gets changed automatically but the fullname doesn't change because email() is a function which is called at the time when we want the email to be returned while fullname is set at the time of initialisation of the object.
If you want to fix the problem for fullname, it can be done by making a function similar to email to get fullname as well. But, this will result in the overhead of changing all the access made to fullname in all the python files which have used the Student class.
Also, creating a function is not the pythonic way of solving this problem. But then what is?

From <https://www.studytonight.com/python/property-in-python> 

Using @property Decorator
Now we will use the @property in the above program to solve the problem of fullname(which we saw above) by creating a getter function for fullname which will allow it to be used as a simple variable and will always return the updated value of fullname property.

"""

print("\nusing @property decorator")


class Students:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):
        return self.fname + ' ' + self.lname

    # generate email using first and last name
    def email(self):
        return f'{self.fname}.{self.lname}@indian.com'


s2 = Students('Tony', 'Stark')
print('Fullname of s1 is: ', s2.fullname)
print('And email address = ', s2.email())

# now updating the s1 object's first name
s2.fname = 'abhinav'
print('Fullname of s2 is ', s2.fullname)
print('And email address = ', s2.email())

print('\n')

"""
In the above example, @property decorator is used on the function named as fullname(). 
Now, this function will work as a fullname attribute and also can work as a getter because of the @property decorator attached to it.
"""

"""
Defining setter and deleter methods with @property Decorator
Similar to the getter method(we have defined in the previous example) we can also define setter and deleter methods for any attribute which is using @property in Python.

The setter method will set the value of the attribute and the deleter method will delete the attribute from the memory.

Let's implement a setter and deleter method for our fullname attribute. 
For defining a setter and deleter method, for an attribute with @property decorator set on its getter method, 
we use a special syntax, where we put @ATTRIBUTE_NAME.setter and @ATTRIBUTE_NAME.deleter decorator on function with name same as the ATTRIBUTE_NAME. 
This is shown in the below example,
"""


class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):
        return self.fname + ' ' + self.lname

    # setter for the fullname
    @fullname.setter
    def fullname(self, name):
        self.fname = name.split(' ')[0]
        self.lname = name.split(' ')[1]

    # deleter for fullname
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Deleted the fullname')

    # generate email using first and last name
    def email(self):
        return f'{self.fname}.{self.lname}@hindustani.com'


s1 = Student('Tony', 'Stark')
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

# now updating the s1 object's first name
s1.fname = 'Steve'
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

# setting new value of fullname
s1.fullname = 'Berry Banner'
print('New Fullname of s1 is ', s1.fullname)

# deleting the fullname
del s1.fullname

"""
In the above example, we have successfully created getter, setter and deleter using the @property decorator.
The simple syntax for creating setter and deleter is:
@attribute_name.(setter/getter/deleter)


The property() function
Instead of using @property decorator, we can use the property() function in python to create getters, setters and deleters in python.

Syntax: property(fget, fset, fdel, doc)

Where the parameters means:

fget(): used to get the value of attribute

fset(): used to set the value of atrribute

fdel() : used to delete the attribute value

doc(): string that contains the documentation (docstring) for the attribute

return: It returns a property attribute from the given getter, setter and deleter.

Below, is an example showing the use of the property() function for the same Student class with the same functions defined as getter, setter and deleter.
"""
print("\nThis time using property() function")


class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + ' ' + lname

    def fullname_getter(self):
        return self.fname + ' ' + self.lname

    def fullname_setter(self, name):
        firstname, lastname = name.split()
        self.fname = firstname
        self.lname = lastname

    def fullname_deleter(self):
        self.fname = None
        self.lname = None
        print('Deleted the fullname.')

    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)

    fullname = property()
    fullname = fullname.getter(fullname_getter)
    fullname = fullname.setter(fullname_setter)
    fullname = fullname.deleter(fullname_deleter)


# this can be done in a single line too
# fullname = property(fullname_getter, fullname_setter, fullname_deleter)


s1 = Student('Tony', 'Stark')
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

# now updating the s1 object's first name
s1.fname = 'Steve'
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

# setting new value of fullname
s1.fullname = 'Berry Banner'
print('New Fullname of s1 is ', s1.fullname)

# deleting the fullname
del s1.fullname
