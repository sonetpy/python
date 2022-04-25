import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print ("Grouping with paranthesis (\d\d\d)-(\d\d\d-\d\d\d\d)")
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print ("######")
print("First group i.e Area Code : ", mo.group(1))
print("Second group i.e Phone number : ", mo.group(2))
print ("Print the entire number :", mo.group(0))
print (mo.group())

#Parentheses have a special meaning in regular expressions, but what do
#you do if you need to match a parenthesis in your text? For instance, maybe
#the phone numbers you are trying to match have the area code set in parentheses.
#In this case, you need to escape the ( and ) characters with a backslash.

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
# Regular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “ Match this pattern three times.” So the slightly shorter regex
print("\nRegular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “ Match this pattern three times.” So the slightly shorter regex")
phoneNumRegex =  re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

