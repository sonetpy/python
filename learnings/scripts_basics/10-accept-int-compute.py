'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''
a = int (input ("how many times you want to enter integers "))
k = 0
i = 1
while (i <= a):
    j = int(input ("enter the numbers"))
    k = j + k
    i = i + 1
print (k)
