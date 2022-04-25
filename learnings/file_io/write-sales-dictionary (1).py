order1 = {'Cheeky Spam': 1.0, 'Chips Spam': 4.0}
order2 = {'Knackered Spam': 1.0}
order3 = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}

menu = open('hotel-menu.txt', 'w')
for key, value in order1.items():
    menu.write(key + ' '+ '$' + str(value) + '\n')

for key, value in order2.items():
    menu.write(key + ' '+ '$' + format(value, '.2f') + '\n')

for key, value in order3.items():
    menu.write(key + ' '+ '$' + format(value, '.2f') + '\n')

menu.close()

read = open('hotel-menu.txt', 'r')
print(read)
read.close()
