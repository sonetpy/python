# Downloading a file from remote machine
from paramiko import SSHClient
from scp import SCPClient
import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = "192.168.1.40"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "my_file.txt"
# get the file size
filesize = os.path.getsize(my_file.txt)

# create the client socket
s = socket.socket()

# Connecting to the server:

print("Connecting to {}:{}".format (host,port))
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
