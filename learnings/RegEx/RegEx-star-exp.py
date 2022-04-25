# Python program to illustrate
# matching a regular expression
# with asterisk(*)
import re
exp=re.compile(r'Bat(wo)*man')
a=exp.search('The Adventures of Batman')
print (a.group())
exp1=re.compile(r'Bat(wo)*man')
mo2 = exp1.search('The Adventures of Batwoman')
print(mo2.group())
exp2=re.compile(r'Bat(wo)*man')
mo3 = exp1.search('The Adventures of Batwowowowoman Batman')
print (mo3.group())

# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))
