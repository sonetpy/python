#Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exericse a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
    }

for name, places in favorite_places.items():
    print ("{} likes the following places:".format(name))
    print ("\t - {}".format(places))
    for place in places:
        print (" - {}".format(place))
