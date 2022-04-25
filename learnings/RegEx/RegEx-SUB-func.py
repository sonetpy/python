import re
txt = "the rain in spain"
exp = re.sub("\s", "$", txt)
print("Subtituting a txt at whitespace\s with $" )
print(exp)

