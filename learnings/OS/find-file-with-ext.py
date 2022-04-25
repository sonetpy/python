# Find a file path with .py .sh .log .xyz etc as extension
import os
import sys
path = input("please enter a path: ")
# check if path exists or not ?
if os.path.exists(path):
    print(os.listdir(path))
else:
    print("Path doesn't exists")
    sys.exit()
# loop under the dir now and see if any file exists with .py or .txt extension
k = os.listdir(path)
for each_files in k:
    for i in each_files:
        if (i == "."):
            print(os.path.join(path,each_files))
        

