name = ''
while not name:
    name = input("enter your name: ")
numofguest = input('How many guests will you have ? ')
if numofguest:
    print ("You should have enough room for {} guests".format(numofguest))
print('Done')
