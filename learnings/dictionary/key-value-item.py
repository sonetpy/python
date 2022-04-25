mycat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

for v in mycat.values():
    print (v)
print ("\n")

for k in mycat.keys():
    print(k)
print("\n")

for k, v in mycat.items():
    print ("{} of my cat is {}".format (k, v))

print ("\n")
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print ("Key: {} Value: {}". format (k, v))

