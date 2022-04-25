class Person:
    def display(self):
        print("I am a person")
    def display(self):
        print("I am a person", self)
    def greet(self):
        print("Hello how are you ?", self)

p1 = Person()
p2 = Person()

p1.display()
p2.greet()

class Person:
    def set_details(self):
        self.name = 'John'
        self.age = 20
    def display(self):
        print("I am a person", self.name)
    def greet(self):
        print("My age is ", self.age)

p1 = Person()
p1.set_details()
p1.display()
p1.greet()


class Person:
    def set_details(self,name,age):
        # self.name is an instance variable where as name is just parameter variable
        # of this method so they are just local variables inside the method.
        # Instance variable attach to instance object and they live as long as the object lives.
        self.name = name
        self.age = age

    def display(self):
        print("I am a person ", self.name)
    def greet(self):
        print("hello, My age is ", self.age)

p1 = Person()
p1.set_details('Abhinav', 20)
p1.display()
p1.greet()
p2 = Person()
p2.set_details('Sam', 30)
p2.display()
p2.greet()

class Person():
    """
    Instance variable can be used anywhere in class.
    # self.name and self.age is an instance variable where as name and age is just
    parameter variable of this method so they are just local variable inside the method.
    """
    def set_details(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am Person ', self.name)
    def greet(self):
        print('I am of AGE', self.age)


p1 = Person()
p1.set_details('Vikrant', 40)
p1.display()
p1.greet()



#Inside the method, self refers to the current instance so the instance variable is prefixed
#with self and dot(.)
#when you refence an instance variable outside of a class, it has to be prefixed
#with the instance name and a dot(.)

class Person():
    def set_details(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am Person ', self.name)
        
    def greet(self):
        if self.age < 80:
            print('hello, how are you doing?')
        else:
            print("Hello, how do you do ? ")
        self.display()

p1 = Person()
p2 = Person()

p1.set_details('Bob', 29)
p2.set_details('Marley', 90)

p1.greet()
p2.greet()
