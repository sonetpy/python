""""
The **kwargs collect all the keyword arguments that are not explicitly defined.
Thus, it does the same operation as *args but for keyword arguments.
**kwargs allow a function to take any number of keyword arguments.
By default, **kwargs is an empty dictionary. Each undefined keyword argument is stored as a key-value pair in the **kwargs dictionary.
https://www.quora.com/How-do-you-resolve-typeerror-getstate-takes-3-positional-arguments-but-4-were-given-Python-development
"""
def foo(a, b, option=True, **kwargs):
    print(a)
    print(b)
    print(option)
    print(kwargs)

# the **kwargs signals that the function may accept keyword arguments, as opposed to positional arguments.
# Keyword arguments are passed as name=value pairs
print(foo(1, 4, 6, param1=5, param2=6, param3=7, param4=8, param5=9, param6=10))

"""
# the **kwargs signals that the function may accept keyword arguments, as opposed to positional arguments.
# Keyword arguments are passed as name=value pairs
"""

def fun(first, second, **kwargs):
    print (first)
    print(second)
    print(kwargs)
fun("one", "two", a=3, b=4, c=5)