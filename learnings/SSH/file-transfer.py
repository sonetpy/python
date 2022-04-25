import paramiko
import tqdm
from paramiko import SSHClient
from scp import SCPClient
host = "192.168.1.40"
port = 22
username = "root"
password = "password"
path = os.path.abspath('test')
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(host, port, username, password, path)

with SCPClient(ssh.get_transport()) as scp:

    scp.put('/Users/kumar.abhinav/test', recursive=True, remote_path='/tmp')

