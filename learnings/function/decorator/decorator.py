'''
In this example, my_decorator is a custom decorator that adds behavior before and after the say_hello function is called. 
When you use the @my_decorator syntax before the say_hello function definition, it means that say_hello will be wrapped by my_decorator, and when you call say_hello(), 
it will actually execute wrapper, which includes the additional behavior defined in the decorator.
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
