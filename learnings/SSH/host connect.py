import paramiko
host = "192.168.1.40"
port = 22
username = "root"
password = "password"
command = "ls -l"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
