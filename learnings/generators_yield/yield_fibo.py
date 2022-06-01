def fibonaci(n):
    a = 1
    b = 1
    for numbers in range(n):
        a, b = b, a+b
        yield a 

for numbers in fibonaci(10):
    print(numbers)