# We can pack and unpack variables using *args and **kwargs.
def foo(*args):
    print (args)

a = [1,2,3]
list(a)
print(foo(a))

b=[1,2,3]
print(foo(b))

# We can pass multiple iterables to be unpacked together with single elements. All values will be stored in the args tuple.
lst = [1,4,5]
tpl = ('a','b',4)
print(foo(*lst, *tpl, 3, 4))

# We can do the packing and unpacking with keyword

def foo1(**kwargs):
    print(kwargs)

# But the iterable that is passed as keyword arguments must be a mapping such as a dictionary.
dct = {'param1':5, 'param2':8}
print(foo1(**dct))


