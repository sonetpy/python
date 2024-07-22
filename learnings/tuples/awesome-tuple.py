# Yes, that's correct! In Python, when a function returns multiple values, they are returned as a tuple. A tuple is a collection of values that can be of any data type, and it's enclosed in parentheses ().
# Yes, when returning multiple values from a function in Python, the returned values are of tuple data types. Tuples are ordered, immutable sequences of Python objects. Tuples are similar to lists, but they cannot be changed. This makes them ideal for storing multiple values that need to be returned from a function.

def main():
    name, house = get_student()
    print (f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()

# Another way to prove is 
def main1():
    student = get_student1()
    print (f"{student[0]} from {student[1]}")

def get_student1():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main1()

# Tuple immutable in nature
# TypeError: 'tuple' object does not support item assignment
def main2():
    student = get_student2()
    if student[0] == "Virat":
        student[1] = "England"
    print (f"{student[0]} from {student[1]}")

def get_student2():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main2()


# If I make a return type as list then you can modify data
def main3():
    student = get_student3()
    if student[0] == "Virat":
        student[1] = "England"
    print (f"{student[0]} from {student[1]}")

def get_student3():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main3()
