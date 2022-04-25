## Use of re.search(r'.at', <statement>)
import re
res=re.search(r'.at','the cat was chasing rat while the bat was looking at them')
print(res.group())

print("\n\n#search() and match() methods only return a single matched substring in the form of the match object.")

print("\n\nWhere '.' is a metacharacter which represents any character accept newline.")

print("\nSo, findall() returns the list of all non-overlapping matches of the patterns.")
import re
res=re.findall(r'.at','the cat was chasing rat while bat was looking at them')
print(res)


