cities = {
    'santiago': {
        'country': 'chile',
        'population': 6310000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975453,
        'nearby mountains': 'himilaya',
        }
    }
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    nearby = city_info['nearby mountains']
    print ("{} is in {}".format(city, country))
    print ("It has a Population of about {} ".format(population))
    print ("The {} mountain are nearby".format(nearby))
    print ("")
