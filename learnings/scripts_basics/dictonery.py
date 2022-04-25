# create a directory
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing items
print ("Accessing Items : ", thisdict["model"])
# There is also a method called .get()
print ("Accessing Items using .get() method: ", thisdict.get("model"))

print ("You can change the value of a specific item by referring to its key name: change the 'year' to 2019")
thisdict["year"] = 2019
print (thisdict)
for i in thisdict:
    print("Using for loop, we are printing the value of the dictionary: ", thisdict.get(i))
# Printing using .values()
for j in thisdict.values():
    print ("This time printing Values as '.value()' : ",j)
# Loop through both keys and values, by using the item() function:
print ("Loop through both keys and values, by using the item() function:")
for x, y in thisdict.items():
    print(x, y)
# Check if key exists
if "model" in thisdict:
    print ("Yes, 'model' is one of the keys in the thisdict dictionary")
# Print length of the dictionery
print(len(thisdict))
# Adding an item in dictionery
thisdict["color"] ="red"
print("After adding 'color = red' in dictionery", thisdict)
# Removing Item
thisdict.pop("model")
print ("The pop() method removes the item with the specified key name: ", thisdict)
thisdict.popitem()
print ("The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead): ", thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print("The del keyword removes the item with the specified key name: ", thisdict)
# Copy of dictionery
mydict = thisdict.copy()
print ("Make a copy of a dictionary with the copy() method:", mydict)


