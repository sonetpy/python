class StateInfo:
    StateName = 'Telangana'
    population = '3.5 crore'

    def func1(self):
        print("Hello from my function")


print(getattr(StateInfo, 'StateName'))

# returns true if object has attribute
print(hasattr(StateInfo, 'population'))

setattr(StateInfo, 'ForestCover', 39)

print(getattr(StateInfo, 'ForestCover'))

print(hasattr(StateInfo, 'func1'))

