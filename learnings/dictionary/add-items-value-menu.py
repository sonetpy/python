menu = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']
menu_prices = {}
price = 0.5
for item in menu:
    menu_prices[item] = 1 + price
    price = price + 1
print(menu_prices)

#output
###############
#{'Knackered': 1.5, 'Pip pip': 2.5, 'Squidgy': 3.5, 'Smashing': 4.5}

print("Printing our menu items and no Prices")
for item in menu_prices:
    print(item)


#output
###############
#Knackered
#Pip pip
#Squidgy
#Smashing

print("Printing our menu items 'keys' and along with Price 'values' ")
for name, price in menu_prices.items():
    print(name, ': $', price, sep='')
#Output
#################
#Knackered: $1.5
#Pip pip: $2.5
#Squidgy: $3.5
#Smashing: $4.5

print("To get a list of the keys in dictionary, use dict_name.keys()")
for x in menu_prices:
    print (x)

print("To get a list of the keys in dictionary, use dict_name.values()")
for items in menu_prices.values():
    print(items)
#output
##############
#1.5
#2.5
#3.5
#4.5


print("\nTo get a list of the keys in dictionary, use dict_name.keys()")
for items in menu_prices.keys():
    print(items)
#Output
#################
#Knackered
#Pip pip
#Squidgy
#Smashing
