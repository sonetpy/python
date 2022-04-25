# search a file with absolute pathname like find command in Linux
import os

listing = os.walk('/home/abhinav/')
filename = input("enter the filename you want to search: ")
for r, d, f in listing:
    for each_file in f:
        if (each_file == filename):
            print(os.path.join(r,each_file))

