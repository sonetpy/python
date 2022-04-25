# https://www.youtube.com/watch?v=kqVQDXfc9hU&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=18
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
"""
try:
    while road_is_clear():
        drive()
except Accident as e:
    take_detour()
"""
"""
x=input("Enter Num1: ")
y=input("Enter num2: ")
z=int(x)/int(y)
print("Division is :", z)
"""
a=input("Enter Num1: ")
b=input("Enter num2: ")
try:
    c = a/int(b)
except ValueError as e:
    print("Exception Occured: you are taking float number, we should take integer ", e)
    c = None
except Exception as e:
    print('éxception type:',type(e).__name__)
    c = None
print("Division is :", c)