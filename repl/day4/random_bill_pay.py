import random
name = ["Jane", "Juliet", "Rob", "Christine"]
h = len(name)
print (h)
ran = random.randint(0, h-1)
print (f"{name[ran]} will have to pay the bill today")