import os
os.chdir("/tmp")
print (os.getcwd())
l=os.rmdir("/tmp/abc")
print ("removed a dir from /tmp/{}".format(l))
os.chdir("/home/abhinav/Python")
print(os.getcwd())

