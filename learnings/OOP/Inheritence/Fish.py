"""
https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
Building a parent class follows the same methodology as building any other class, except we are thinking about what methods the child classes will be able to make use of once we create those.
"""
class Fish:
    def __init__(self, first_name, last_name="Fish",skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


...


class Trout(Fish):
    pass

"""
We have created a Trout object terry that makes use of each of the methods of the Fish class even though we did not define those methods in the Trout child class. 
We only needed to pass the value of "Terry" to the first_name variable because all of the other variables were initialized.
"""

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

"""
Next, let’s create another child class that includes its own method. We’ll call this class Clownfish, and its special method will permit it to live with sea anemone:
"""
...


class Clownfish(Fish):

    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


...
casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()