import re
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

print("\n Matching Specific Repetitions with Curly Brackets ")
ha3 = re.compile(r'(ha){3}')
ha35 = re.compile(r'(ha){3, 5}')
mo2 = ha3.search('What the hell why are you doing hahaha')
mo3 = ha35.search("how many time I did hahahaha hahaha")
print (mo2.group())


