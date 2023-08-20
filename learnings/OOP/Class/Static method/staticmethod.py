# https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-58
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
#In the expression *string.split("-"), the star (*) is a wildcard character. It means that the string can be any value, including the empty string.
# So, the expression will return a list of all the substrings of the string, separated by the hyphen character (-).
#For example, if the string is "hello-world", the expression will return the list ["hello", "world"].

    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")


