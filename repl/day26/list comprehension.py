""""Print sqr of the numbers"""
numbers = [1, 2, 3, 4, 5]
print([(i * 2) for i in numbers])

""""print all names in CAPS which is of 4 letters"""
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elon', 'Freddie']
long_names = [ i.upper() for i in names if len(i) == 4 ]
print(long_names)