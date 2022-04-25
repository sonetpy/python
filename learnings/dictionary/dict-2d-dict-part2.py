#Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

#Note: When I decided to post solutions and wrote complete programs to solve each exercise, I realized this problem was not as well phrased as it should have been. It doesn’t really make sense to name each dictionary for the pet it describes; that information should really be included in the dictionary, rather than being used as the name of the dictionary. This solution reflects that approach.

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for p in pets:
    print ("Here's what I know about ", p['name'])
    for key, value in pet.items():
        print ("\t {}: {}".format(key,value))
