t = tuple(['cat', 'dog', 5])
print ("Tupel : ",t)
# converting into list
l = list(('cat', 'dog', 5))
print ("List : ", l)

list ('hello')
print (list ('hello')) 


# Another Example
t = ('USA','JAP','IND')
print(t)
l = t
k = list(l)
print(list(l))
print(k)
k.append('GER')
print(k)

# Output
"""
('USA', 'JAP', 'IND')
['USA', 'JAP', 'IND']
['USA', 'JAP', 'IND']
['USA', 'JAP', 'IND', 'GER']
"""