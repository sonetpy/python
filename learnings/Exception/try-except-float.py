#We can also use try, except in other situations that might have unexpected problems… like casting user input to a number.
price = input ("enter the price: ")
try:
    price = float(price)
    print('Price =', price)
except ValueError:
    print('Not a number! ')
print("\nStoring the Eception's error msg")
price = input ("enter the price: ")
try:
    price = float(price)
    print('Price =', price)
except ValueError as err:
    print(err)