# Find a file who has no owner and delete those files.
import os
uidset = set()
for lines in open("/etc/passwd"):
    split = lines.split(":")
    uidset.add(int(split[2]))

listing = os.walk('/home/abhinav/Python/Json-CSV')
for root_path, directories, files in listing:
     #print("root path =", root_path)
     #print("directories =", directories)
     #print("files =", files)
     for i in files:
         path = root_path + "/" + i
         attributes = os.stat(path)
         if attributes.st_uid not in uidset:
             print(path + " has no owner")

print ("\nnew code")

#!/usr/bin/env python
import os
import pwd
filename = '/etc/passwd'
st = os.stat(filename)
uid = st.st_uid
print(uid)
# output: 0
userinfo = pwd.getpwuid(st.st_uid)
print(userinfo)
# output: pwd.struct_passwd(pw_name='root', pw_passwd='x', pw_uid=0,
#          pw_gid=0, pw_gecos='root', pw_dir='/root', pw_shell='/bin/bash')
ownername = pwd.getpwuid(st.st_uid).pw_name
print(ownername)
# output: root

