from paramiko import SSHClient
from typing import Tuple

USERNAME="tom"
HOSTNAME="192.168.40.247"

def main():
    ssh = sshClient(HOSTNAME, USERNAME)
    print(ssh.run("dir"))

class sshClient():
    def __init__(self, hostname: str, username: str) -> SSHClient:
        self._ssh = SSHClient()
        self._ssh.load_system_host_keys()
        self._ssh.connect(hostname=hostname, username=username)

    def run(self, command: str) -> Tuple[str, str, str]:
        return self._ssh.exec_command(command)

if __name__ == "__main__":
    # execute only if run as a script
    main()