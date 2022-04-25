import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

import re
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

import re
batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman')== None
print(mo3)
