import os
print("change dir using os.chdir() ")
os.chdir("/home/abhinav")
print(os.getcwd())
os.chdir("/home/abhinav/Python")
print(os.getcwd())
#
print ("In order to set the current directory to the parent directory use '..' as the argument in the chdir() function.")
os.chdir("..")
print(os.getcwd())

