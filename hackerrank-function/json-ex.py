import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) #Load JSON data from a string.

# the result is a Python dictionary:
print(y["age"])