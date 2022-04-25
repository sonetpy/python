#  Write a Python program to check whether a file exists

with open('myfile.txt', mode='r') as new_file:
    if new_file:
        print ("file present")
    else:
        print ("file not present")


