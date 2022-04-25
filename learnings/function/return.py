def example(start, end):
    ele = list(range(start, end))
    return ele


print(example(5, 10))

######### Swap
def swap(a, b):
    return b, a

a = 2
b = 5

x, y = swap(a, b)
print(x,',', y)

z = swap(a, b)
print(z)
