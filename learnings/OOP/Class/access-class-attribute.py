class Parrot:
    # class attribute
    species = "bird"
    # instance attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"name: {self.name}\n age: {self.age}\n")

    @classmethod
    def newspecies(cls,new_species):
        cls.species=new_species

    def details_if_changed(self):
        print(f"this is the new species {Parrot.species} assigned to {self.name} with age {self.age}")


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


blu.details()
print("Blue is a ", getattr(Parrot,'species'))

blu.newspecies("animal")
blu.details_if_changed()

print("Blue is ", getattr(Parrot,'species'))
