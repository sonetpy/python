"""
You can assign a multiline string to a variable by using three quotes:
"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

""""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""
a = "Hello, World!"
print(a[1])

# Check String :: To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

'''
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("yes, 'expensive' is NOT present")
