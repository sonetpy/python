#Let’s use continue to write a program that asks for a name and password.Enter the following code into a new file editor window and save the program as swordfish.py.
# if the username is 'Joe' and password as 'swordfish' then print "permission granted"
while True:
    name = input("What is your name :")
    if name != 'Joe':
        continue
    else:
        password = input("enter your password: ")
        if password == 'swordfish':
            break
print("Access granted")

