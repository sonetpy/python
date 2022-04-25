# Example 1
print("# Example 1")
class Person:
    def __init__(self):
        print("This is person from base class")


class Student(Person):
    def __init__(self):
        super().__init__()
        print("This is Student from derived class")


st = Student()
# Now see what happens if I use super().__init__() after print stmt in Student class.

# Example 2
print("# Example 2")
class Person:
    def __init__(self):
        print("This is person from base class")


class Student(Person):
    def __init__(self):
        print("This is Student from derived class")
        super().__init__()

st = Student()

# Example 3
print("# Example 3")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email

st = Student('virat', 33, 'virat@gmail.com')
print(st.name)
print(st.age)
print(st.email)