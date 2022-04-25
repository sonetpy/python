a = [1, 2, 3, 4]
b = a
c = a[:]
print("\nexample of shallow copy")
print (a)
print(b)
print(c)
a[2]=99
print("\nexample of deep copy")
print(a)
print(b)
print(c)

for i in range (1, 10):
    if i == 6:
        break
    print(i, ', ', sep='', end='')
print()