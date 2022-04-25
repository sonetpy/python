def myfun(money):
    return money


print(myfun(500))
print("Now a function alias")
dollar = myfun
print(dollar(700))


def sonu(*args, **kwargs):
    print(args)
    print(kwargs)


sonu('a', 'b', a=1, b=2)
