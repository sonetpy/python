favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

#print each person’s name along with their favorite numbers.
for name, num in favorite_numbers.items():
    print ("{} likes the following numbers:".format(name))
    for n in num:
        print (" ",n)
