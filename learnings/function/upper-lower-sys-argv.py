'''string=input("Enter a string :")
action=input("lower/upper/title :")
if (action == "lower"):
    print(string.lower())
elif (action == "upper"):
    print(string.upper())
elif (action == "title"):
    print(string.title())
'''
# similar code here but with sys.argv
import sys
if (len(sys.argv) != 3):
    print ("We need 3 items"); sys.exit()

string = (sys.argv[1])
action = (sys.argv[2])
if (action == "lower"):
    print(string.lower())
elif (action == "upper"):
    print(string.upper())
elif (action == "title"):
    print(string.title())

