orders = []
order = input("What would you like to order? (Q to Quit) and Y for Yes")
while order.upper() != 'Q': #Always run the loop forever
    if order.upper() == 'Q':
        break
    else:
        order = input ("Anything else ? (Q to Quit)")
        orders.append(order)
print(orders)

### OR

orders = []
order = input("What would you like to order? (Q to Quit) and Y for Yes")
while True:
    if order.upper() == 'Q':
        break
    order = input("Anything else Q for quit :")
    orders.append(order)
print (orders)
