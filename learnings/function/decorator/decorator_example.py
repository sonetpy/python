## Normal nestead function
def compose(f, g, x):
    return f(g(x))

compose(print, len, "hello, world!")

### another example
def a():
    def b(x):
        print (f'hey chu {x}')
        return 
    return b

j = a()
j('tiya')

#### Another example ###
import random
def random_power():
    ### Nestead functions
    def f(x):
        return x**2
    def g(x):
        return x**3
    def h(x):
        return x**4
    
    functions = [f,g,h]
    return random.choice(functions)

for i in range(10):
    p = random_power()
    print(p(3))

