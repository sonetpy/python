'''The findall() Function
The findall() function returns a list containing all matches.

Example
Print a list of all matches:'''

import re
txt = "The rain is Spain"
x = re.findall("ai", txt)
print (x)

'''
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:
'''
# Search for the first white-space character in the string:
import re
txt = "The rain in Spain"
x = re.search("Spain", txt)
if x:
    print("I can see the word Spain in the sentence")

'''
The split() Function
The split() function returns a list where the string has been split at each match:

Example
Split at each white-space character:
'''

import re
txt = "The rain in Spain"
k = re.split(" ", txt)
l = re.split("\s", txt)
x = re.split("\s", txt, 1)
print (k)
print (l)
print(x)



