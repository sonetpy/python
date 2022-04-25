#Write a python program to check whether the given key is present, if present print the value , else add a new key and value
# https://www.zframez.com/tutorials/python-tutorial-and-exercises-p5.html

b = dict (joe = 90 , peter = 85 , jack = 88)
if ('joe' in b):
    print (b['joe'])
else:
    b['joe'] = 75
    print (b)

# Another Example
c = dict (joe = 90 , peter = 85 , jack = 88)
if ('abhinav' in c):
    print (c['abhinav'])
else:
    c['abhinav'] = 35
    print (c)

