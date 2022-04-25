"""
How to access a Variable defined in a Scope of a class but outside of Method.
"""
class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


def main():
    s1 = Student()
    s2 = Student()
    s3 = Student()
    print('The number of Student is ', Student.count)


if __name__ == "__main__":
    main()
