"""
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