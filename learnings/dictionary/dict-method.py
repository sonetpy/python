# https://www.zframez.com/tutorials/python-tutorial-and-exercises-p5.html

# Create a Dictionary
a = dict (joe = 90 , peter = 85 , jack = 88)
print (a)

# Add an item to dictionary
a['kris'] = 85
print (a)

# Delete an item
del a['kris']
print (a)

# Checking whether key is present
'peter' in a

#Print a value of Peter
print (a.get('peter',0))
print (a.get('peter'))

# Print KEY
print (a.keys())

#Print Values
print (a.values())
print (list(a))

