# The included code stub will read an integer, , from STDIN.
#
# Without using any string methods, try to print the following:

def printfun(n):
    if n < 151:
        for i in range(1, n+1):
            print(i, end = '')

j = int(input("enter a num :"))
printfun(j)

