# We can use both *args and **kwargs in a function but *args must be put before **kwargs.
def foo(a,b,*args,**kwargs):
    print (a,b)
    print(args)
    print(kwargs)
print (foo(1, 4, 6, 5, param1=5, param2=6))