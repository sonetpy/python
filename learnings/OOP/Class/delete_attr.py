class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)
# creating object of the class
obj = Fruit("Apple", "red")
obj.show()
# Deleting Object Properties
del obj.name

# Accessing object properties after deleting
print(obj.name)

