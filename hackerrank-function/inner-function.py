def myfun():
    x = 300
    def myinnerfun():
        print ("the value of X = {}".format(x))
    myinnerfun()

print (myfun())

