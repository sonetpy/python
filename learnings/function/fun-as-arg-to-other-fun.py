# To visualize the code use the link https://pythontutor.com/render.html#mode=display

def plus_one(number):
    print (number + 1)

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
'''
abhinku@k8s:~$ python3 /tmp/num_ex.py
> /tmp/num_ex.py(10)<module>()
-> function_call(plus_one)
(Pdb) step
--Call--
> /tmp/num_ex.py(5)function_call()
-> def function_call(function):
(Pdb)
> /tmp/num_ex.py(6)function_call()
-> number_to_add = 5
(Pdb)
> /tmp/num_ex.py(7)function_call()
-> return function(number_to_add)
(Pdb)
--Call--
> /tmp/num_ex.py(2)plus_one()
-> def plus_one(number):
(Pdb)
> /tmp/num_ex.py(3)plus_one()
-> print (number + 1)
(Pdb)
6
--Return--
> /tmp/num_ex.py(3)plus_one()->None
-> print (number + 1)
(Pdb)
--Return--
> /tmp/num_ex.py(7)function_call()->None
-> return function(number_to_add)
(Pdb)
--Return--
> /tmp/num_ex.py(10)<module>()->None
-> function_call(plus_one)
(Pdb)
'''



# Another example ###
# import pdb --->> Code tracing module

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

# pdb.set_trace() --->> this is to trace a code
greet(shout)
greet(whisper)

'''
abhinku@k8s:~$ python3 /tmp/pycode.py
> /tmp/pycode.py(14)<module>()
-> greet(shout)
(Pdb) step
--Call--
> /tmp/pycode.py(9)greet()
-> def greet(func):
(Pdb)
> /tmp/pycode.py(10)greet()
-> greeting = func("Hi, I am created by a function passed as an argument.")
(Pdb)
--Call--
> /tmp/pycode.py(3)shout()
-> def shout(text):
(Pdb)
> /tmp/pycode.py(4)shout()
-> return text.upper()
(Pdb)
--Return--
> /tmp/pycode.py(4)shout()->'HI, I AM CRE... AN ARGUMENT.'
-> return text.upper()
(Pdb)
> /tmp/pycode.py(11)greet()
-> print(greeting)
(Pdb)
HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
--Return--
> /tmp/pycode.py(11)greet()->None
-> print(greeting)
(Pdb)
> /tmp/pycode.py(15)<module>()
-> greet(whisper)
(Pdb)
--Call--
> /tmp/pycode.py(9)greet()
-> def greet(func):
(Pdb)
> /tmp/pycode.py(10)greet()
-> greeting = func("Hi, I am created by a function passed as an argument.")
(Pdb)
--Call--
> /tmp/pycode.py(6)whisper()
-> def whisper(text):
(Pdb)
> /tmp/pycode.py(7)whisper()
-> return text.lower()
(Pdb)
--Return--
> /tmp/pycode.py(7)whisper()->'hi, i am cre... an argument.'
-> return text.lower()
(Pdb)
> /tmp/pycode.py(11)greet()
-> print(greeting)
(Pdb)
hi, i am created by a function passed as an argument.
--Return--
> /tmp/pycode.py(11)greet()->None
-> print(greeting)
(Pdb)
--Return--
> /tmp/pycode.py(15)<module>()->None
-> greet(whisper)
(Pdb)
'''

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