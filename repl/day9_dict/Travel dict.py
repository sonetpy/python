travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#DO NOT change the code above 👆

#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

#Do not change the code below 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


interface = ['Ethernet0', 'Ethernet1', 'Serial0', 'Serial1']
ip = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
status = ['up', 'down', 'up', 'up']

#How to iterate over 2+ lists at the same time
db = zip(interface, ip, status)
print (db)
print (" \t\t\tInterface\t\t\tIP\t\t\tStatus")
k = 0
for interface, ip, status in db:
    k = k + 1
    print ("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(k, interface, ip, status))
