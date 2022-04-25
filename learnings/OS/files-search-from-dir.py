import os
myfiles =['accounts.txt', 'details.txt', 'invite.txt']
for filename in myfiles:
    print(os.path.join('/home/abhinav/Python/import-OS', filename))

