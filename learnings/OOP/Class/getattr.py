# Example 1
class Student:
    marks = 10

    def report_card(self, name):
        self.name = name
        print(f'{self.name} marks is {Student.marks}')


s = Student()
# first way of accessing attribute data
s.report_card('student')
# Second way of accessing Attribute data
print(getattr(Student, 'marks'))
# Third way of accessing Attribute data
print(s.marks)
print('Forthways of printing attribute',Student.marks)

# Example 2
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


#Example 3
class Parrot:
    # class attribute
    species = "bird"
    # instance attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Blu is a", getattr(Parrot, 'species'))
print('Blu is a Parrot.species ', Parrot.species)

print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))