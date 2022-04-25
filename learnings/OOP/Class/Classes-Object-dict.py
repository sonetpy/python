"""
Python maintains different dictionaries for classes and objects.
Class dictionary includes information on class attributes
Object dictionary holds information on instance attributes.
"""
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

def main():
    p = Person('John')

    print(Person.__dict__)
    print(p.__dict__)

if __name__ == '__main__':
    main()
