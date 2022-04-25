def num(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

print(num(10))

# yield function
def yld(n):
    for i in range(n):
        yield i**2

for x in yld(10):
    print (x)