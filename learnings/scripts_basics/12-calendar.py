'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.'''

import calendar
m = int (input("enter month : "))
y = int (input("enter year : "))
print (calendar.month(y, m))