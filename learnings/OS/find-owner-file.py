#!/usr/bin/env python
import os
import pwd
filename = "/home/abhinav/Python/Json-CSV"
for root_path, directories, files in os.walk("/home/abhinav/Python/Json-CSV"):
    for i in files:
        if os.path.islink(i):
            continue
        st = os.stat(i)
        uid = st.st_uid
        print(uid)
        userinfo = pwd.getpwuid(st.st_uid)
        print(userinfo)
        ownername = pwd.getpwuid(st.st_uid).pw_name
        print(ownername)


        

