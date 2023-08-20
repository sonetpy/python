# Define a class called Person
class Person:
    # Define the constructor method that initializes the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method that prints a greeting message
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
p1 = Person("Alice", 25)

# Define a function that takes an object of the Person class as an argument
def introduce(person):
    # Call the greet method of the person object
    person.greet()


# Call the introduce function with the p1 object as the argument
introduce(p1)

