def option(a, b, *args, option=True):
    r = 0
    if option:
        for i in args:
            r = r + a + b + i
            r = r + 1
        return r
    else:
        print ("bye")

print (option(10,20,30,40,50,60))
print(option(10,20,40,50,option=False))

#1442 sell
#1372 sell