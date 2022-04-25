'''Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''

a = []
k = int(input("enter the number to iterate : "))
for i in range(0, k):
    z = int(input("enter a number : "))
    a.append(z)
l = int(input("enter the number to check : "))
if l in a:
    print("True")
else:
    print("false")


