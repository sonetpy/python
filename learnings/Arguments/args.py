""""
*args allow a function to take any number of positional arguments.
"""
def addition(*args):
    result = 0
    for i in args:
        result += i
    return result

print(addition(10,20))


def sonu(*args, **kwargs):
    print(args)
    print(kwargs)


sonu('a', 'b', a=1, b=2)