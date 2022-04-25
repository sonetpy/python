'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
a = input ("enter numbers comma seperated ")
list = a.split(',')
tuple = tuple(list)
print ("list :", list)
print ("tuples : ", tuple)




