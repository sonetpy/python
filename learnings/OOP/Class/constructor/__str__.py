class Students:
    def __init__(self, name):
        self.name = name

s1 = Students('abhinav')
print(s1)

class Students:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student[' + self.name + ']'

s2 = Students('john')
print(s2)

