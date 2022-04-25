#Program to find the highest UID from /etc/passwd file"
import os
maxuid=0
for line in open("/etc/passwd"):
    split = line.split(":")
    if int(split[2]) > maxuid:
        maxuid = int(split[2])
print(maxuid)

