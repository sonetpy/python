def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

function = operations["+"]

num1 = int(input("enter num1"))
num2 = int(input("enter num2"))



