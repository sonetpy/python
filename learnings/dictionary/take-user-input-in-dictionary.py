menu = {}
for i in range(3):
    ### Enter the food item and Price
    food = str(input("Enter the food item : "))
    price = int(input ("enter the price of a food $"))
    menu.update({food:price})

print("\nUpdated Dictionary is :")
print(menu)

