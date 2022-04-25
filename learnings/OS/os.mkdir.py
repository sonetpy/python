import os
dir_name = input("enter a dir name to be created : ")
pwd = "/home/abhinav/Python/import-OS"
path = os.path.join(pwd, dir_name) 
os.mkdir(path)
print ("the dir {0} has been created at {1}".format(dir_name, path))  
print ("the dir {} has been created at {}".format(dir_name, path))

