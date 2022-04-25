# https://www.youtube.com/watch?v=ttMX3Ns_0oY
# Multiple Inheritance
class Father:
    def gardening(self):
        print("I enjoy Gardening")

class Mother:
    def cooking(self):
        print("I love Cooking")

class Child(Father, Mother):
    def sports(self):
        print("I love cricket")

c = Child()
c.gardening()
c.cooking()
c.sports()

##### Another way of coding
print("\nThis child hase below skills from father and Mother")
class Father:
    def skills(self):
        print("Coding and Gardening")

class Mother:
    def skills(self):
        print("Art and Craft")

class Child:
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Love playing Cricket")

c = Child()
c.skills()
