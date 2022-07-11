# Only one unpack operation allowed in list
d = [1,2,3,4,5,6]
a,*b,c =d
print(a)
print(*b)
print(c)


"""
1
2 3 4 5
6
"""