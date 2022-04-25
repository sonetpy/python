import math
def paint_area(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans} cans of paint to paint wall")

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_area(height=test_h, width=test_w, cover=coverage)

def greet(name, location):
    print(f"your name is {name}")
    print(f"you are from {location}")

greet(name='abhinav', location='finland')