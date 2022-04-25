"""
hasattr() method takes two parameters:

object - object whose named attribute is to be checked
name - name of the attribute to be searched
"""

class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
