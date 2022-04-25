import os
import sys

k=os.access("testrename", os.F_OK)
if k:
    path = os.getcwd()
    print ("The path of the file 'testrename' is at :", path)
#print("\n\n Change the permission to RO : \n")
#print(os.system('ls -lah | grep testrename'))
#print("\n changing the permission of the file 'testrename' RWX : \n")
#l=os.access('testrename', os.X_OK)
#if l:
#    print("\n the file 'testrename' has execute permission ")
print(os.system('ls -lah|grep testrename'))
print("\n change the permission of the file to 247 chmod()\n ")
os.chmod('testrename', 247)
print(os.system('ls -lah|grep testrename'))
print("\nchanging the ownership of the file now using chown() to root user from abhinav ")
print(os.chown('testrename', 0, 0))
print(os.system('ls -lah|grep testrename'))

