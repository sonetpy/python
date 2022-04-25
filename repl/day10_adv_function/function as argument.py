# https://www.kite.com/python/answers/how-to-pass-a-function-in-another-function-in-python
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(add(2, multiply(5, divide(8, 4))))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

import math


def paint_area(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans} cans of paint to paint wall")


test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_area(height=test_h, width=test_w, cover=coverage)