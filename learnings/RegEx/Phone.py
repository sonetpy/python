'''Say you want to find a phone number in a string. You know the pattern:
three numbers, a hyphen, three numbers, a hyphen, and four numbers.
Here’s an example: 415-555-4242.
Let’s use a function named isPhoneNumber() to check whether a string
matches this pattern, returning either True or False.'''

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
msg=input("enter a msg and a phone number : ")
for i in range(len(msg)):
    chunk = msg[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print ('done')


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

def phone(text):

    if len(text) != 12:
        return False
    for i in range (0, 3):
        if text[i].isdecimal():
            return True
    if text[3] == '-':
        return True
    for i in range(4, 7):
        if text[i].isdecimal():
            return True
    if text[7] == '-':
        return True
    for i in range (8, 12):
        if text[i].isdecimal():
            return True
    return False


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
