for each in [3,4,56,7,8]:
    break
    print(each)

print("after loop")
print("======================")
for each in [3,4,56,7,8]:
    print(each)
    if each==56:
        break
print("after loop")
print("========================")

paths=['/usr/bin','/usr/bin/httpd','home/users/xyz/weblogic/config.xml']
for each_path in paths:
    print("now working on: ", each_path)
    if 'httpd' in each_path:
        print(each_path)
        break ## This will break the loop and will not loop further once it gets 'httpd'
