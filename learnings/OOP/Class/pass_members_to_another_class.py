# Passing Members of one class to another Class

class Students:
    #Constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # Instance Method
    def disp(self):
        print("Student name:", self.name)
        print("Student roll:", self.roll)

class User:
    # Static Method
    @staticmethod
    def show(s):
        print("Student: ", s.name)
        print("Roll: ", s.roll)
        s.disp()

# Creating object of Student Class
stu = Students('Rahul', 33)
User.show(stu)

