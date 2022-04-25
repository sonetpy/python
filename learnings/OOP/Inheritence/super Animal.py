class Animal:
    # Initializing Constructor
    def __init__(self):
        self.leg = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

    def isMammal(self):
        if self.mammals:
            print("It is Mammal")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal")


class Dogs(Animal):
    def __init__(self):
        super().__init__() #This will take you to Animal class and Initialize

    def __int__(self):
        super().isMammal() #this will use the isMammal Method


class Horses(Animal):
    def __init__(self):
        super().__init__() #This will take you to Animal class and Initialize

    def hasTailandLegs(self):
        if self.tail and self.leg == 4:
            print("Has legs and Tails")


Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()


# Example 2 of Multiple Inheritance

class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):

    def __init__(self, name):
        # Calling the constructor
        # of both thr parent
        # class in the order of
        # their inheritance
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")
