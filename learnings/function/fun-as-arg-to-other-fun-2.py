# Python code visualizer https://pythontutor.com/render.html#mode=display
# Define higher order function
def fun(foo):
    result = foo('Welcome To AskPython!!')
    return result

# Define function-1
def fun1(str):
    return str.lower()

# Define function-2
def fun2(str):
    return str.upper()

# Pass funtion-1 as an argument
# to fun() function
print(fun, fun1)

str1 = fun(fun1)
print(str1)

# Pass funtion-2 as an argument
# to fun() function
str2 = fun(fun2)
print(str2)