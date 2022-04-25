# Defining Class
class Phone:
    #  Inside classes, you can define functions or methods that are part of this class
    def make_call(self):# Calling Method
        print("making phone call")
        """NOTE: About using “self” in Python

The self-argument refers to the object itself. Hence the use of the word self. So inside this method, self will refer to the specific instance of this object that’s being operated on.
Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python. It is part of the Python syntax to access members of objects""""

    def play_game(self): # Calling Method
        print("playing game")

# Instantiating the p1 object.  To make an object of the class
p1 = Phone()
# To call a method in a class
p1.make_call()
p1.play_game()

