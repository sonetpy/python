"""Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example
Convert the tuple into a list to be able to change it:
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

"""
Add Items
Once a tuple is created, you cannot add items to it.

Example
You cannot add items to a tuple:
"""
thistuple = ("apple", "banana", "cherry")
thistuple.append("orange") # This will raise an error
print(thistuple)

"""
Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

Example
Convert the tuple into a list, add "orange", and convert it back into a tuple:
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

"""
Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

Example
Convert the tuple into a list, remove "apple", and convert it back into a tuple:
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print (thistuple)

"""
Or you can delete the tuple completely:

Example
The del keyword can delete the tuple completely:
"""
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists