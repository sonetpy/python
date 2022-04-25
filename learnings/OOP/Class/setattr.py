# The setattr() function sets the value of the attribute of an object.
class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

# set value of name to Adam
setattr(person, 'name', 'Adam')
print(person.name)

# set value of marks to 78
setattr(person, 'marks', 78)
print(person.marks)

#Example 2

class Person:
  name = 'Adam'


p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)

# Example 3
class Person:
  name = 'Adam'


p = Person()

# setting attribute name to John
setattr(p, 'name', 'John')
print('Name is:', p.name)

# setting an attribute not present in Person
setattr(p, 'age', 23)
print('Age is:', p.age)