first_item = {'name': 'Spam n Eggs',
'description': 'Two eggs with Spam',
'price':2.50}
second_item = {'name': 'Spam n Jam',
'description': 'Biscuit with Jam with Spam',
'price':3.50}
#Remember: first access the outer list, then access the dictionary key.
menu_items = [first_item, second_item]
print(menu_items[0]['name'], menu_items[0]['price'], menu_items[0]['description'])
print(menu_items[1]['name'], menu_items[1]['price'], menu_items[1]['description'])

