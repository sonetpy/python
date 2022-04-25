print("Welcome to the love calculator")
name1 = input("What is your name? ")
name2 = input("What is your name? ")
name = ('{} {}'.format(name1, name2))
love = "true love"
count = -1
count1 = 0
count2 = 0
for i in love:
    if name.count(i):
        count += 1

print("This is the number of count {} of the occurances of True Love in {} and {}".format(count, name1, name2))

for j in love:
    if name1.count(j):
        count1 += 1
print(count1)
for k in love:
    if name2.count(k):
        count2 += 1

print(count2)

"""
l1 = "true"
l2 = "love"

index1 = n1low.count("t")
j1 = n2low.count("t")
index2 = n1low.count("r")
j2 = n2low.count("r")
index3 = n1low.count("u")
j3 = n2low.count("u")
index4 = n1low.count("e")
j4 = n2low.count("e")
index = index1+index2+index3+index4+j1+j2+j3+j4

j1 = n2low.count("l")
index1 = n1low.count("l")
j2 = n2low.count("o")
index2 = n1low.count("o")
j3 = n2low.count("v")
index3 = n1low.count("v")
j4 = n2low.count("e")
index4 = n1low.count("e")
j = (j1+j2+j3+j4+index1+index2+index3+index4)
print ("Love percentage is : {}{}".format(index,j))
"""
