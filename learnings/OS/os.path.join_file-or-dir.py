# Find out whether it is a file or dir in a given path
import os
path = input ("enter a path: ")
if os.path.exists(path):
    print(os.listdir(path))
else:
    print("Path doesn't exists")
    sys.exit()
# iterate on a list
files=os.listdir(path)
for each_file in files:
    k=os.path.join(path,each_file)
    if os.path.isdir(k):
        print ("dir \t  {}".format(each_file))
    else:
        print ("file  \t  {}".format(each_file))

