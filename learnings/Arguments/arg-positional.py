def value_printer(a, b, *args):
    print ("the value of a :{}".format(a))
    print ("The value of b :{}".format(b))
    x = 0
    for i in args:
        print ("The additional value is at index {} is :{}".format(x,i))
        x = x + 1

print(value_printer(1, 2, 5, 9, 4, 22))

"""
Consider the following example:
arg_printer(a=4, 2, 4, 5)
SyntaxError: positional argument follows keyword argument
If we assign a value to a positional argument, it becomes a keyword argument. Since it is followed by positional arguments, we get a SyntaxError.
"""

