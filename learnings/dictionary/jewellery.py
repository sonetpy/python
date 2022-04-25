inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
inventory['pocket'] = {'seashell', 'strange berry', 'lint'}
print (inventory)
#.sort()the items in the list stored under the 'backpack' key.
print ("\n", inventory['backpack'].sort())

