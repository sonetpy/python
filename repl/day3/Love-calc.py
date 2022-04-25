print("Welcome to the love calculator")
name1 = input("What is your name? ")
name2 = input("What is your name? ")
n1low = name1.lower()
n2low = name2.lower()
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

