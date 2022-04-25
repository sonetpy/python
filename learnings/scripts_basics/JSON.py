# Convert from JSON to Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
x = {"name": "John",
  "age": 30,
  "city": "New York"}
# convert into JSON:
y = json.dumps(x)
print(y)

#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a Python object containing all the legal data types:

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

#Format the Result
#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

#The json.dumps() method has parameters to make it easier to read the result:

#Example
#Use the indent parameter to define the numbers of indents:

print(json.dumps(x, indent=4))

#Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print("######################")
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, sort_keys=True))
