#Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
# https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/

# make empty list to store people in
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }

people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)
person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
    }
people.append(person)

print (people)
print ("")
for i in people:
    name1 = (i['first_name'])
    name2 = (i['last_name'])
    age = (i['age'])
    city = (i['city'])
    print ("{} {} from {} has age {}". format(name1,name2,city,age))
