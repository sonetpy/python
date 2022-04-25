import os
#for file in os.listdir("."):
os.chdir("/home/abhinav/Python")
for file in os.listdir("."):
    info = os.stat(file)
    print(file, info.st_size)

