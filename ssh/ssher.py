"""
###### CREATOR          Ted
###### DESCRIPTION      SSH tool for executing command and transporting file
                        [TBD]
###### VERSION          v1.0
###### UPDATE           2016/01/21

Configuration File Format:

192.168.86.86|22|root|hello|/tmp
#192.168.86.86|22|admin|admin|/tmp
10.0.0.111|22|admin|admin|/home/ted
"""

import re
import os
import sys
import getopt
import socket
import os.path
import paramiko


class SSHer(object):
    CONFIG_FILE = "host.conf"
    DEFAULT_PORT = 22
    CONNECTION_TIMEOUT = 5

    def __init__(self):
        # Read and parse configuration
        self.hosts = []
        self._parse_config()

        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute(self, mode, item):
        if mode == "command":
            for host in self.hosts:
                self._command(item, **host)

        # mode == "transport"
        else:
            for host in self.hosts:
                self._transport(item, **host)

    def _parse_config(self):
        keys = ["IP", "PORT", "USERNAME", "PASSWORD", "REMOTE"]
        try:
            with open(self.CONFIG_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or re.match('^$', line):
                        continue

                    data = line.split('|')
                    host = dict(zip(keys, data))
                    self.hosts.append(host)

        except IOError:
            sys.exit("{} is not found".format(self.CONFIG_FILE))

    def _command(self, command, **kwargs):
        """
        Execute a command on remote host

        :param command: Command, like "ps -ef"
        :param kwargs: dict type, {
                                    "IP": "192.168.1.1",
                                    "PORT": 22,
                                    "USERNAME": "ted",
                                    "PASSWORD": "hello"
                                }
        :return: None
        """
        ip = kwargs["IP"]
        port = int(kwargs["PORT"])
        username = kwargs["USERNAME"]
        password = kwargs["PASSWORD"]

        try:
            self._ssh.connect(ip, port, username, password, timeout=self.CONNECTION_TIMEOUT)
            stdin, stdout, stderr = self._ssh.exec_command(command)

            self._colored_print(ip)
            for line in stdout:
                print(line.rstrip())
            for line in stderr:
                print(line.rstrip())

        except paramiko.SSHException as err:
            self._colored_print(ip, msg_type="error", msg=str(err))
        except socket.error as err:
            self._colored_print(ip, msg_type="error", msg=str(err))

    def _transport(self, local, **kwargs):
        """

        :param local: local file or directory
        :param kwargs: {
                            "IP": "192.168.1.1",
                            "PORT": 22,
                            "USERNAME": "ted",
                            "PASSWORD": "hello"
                            "REMOTE": "/tmp"
                       }
        :return:
        """
        ip = kwargs["IP"]
        port = int(kwargs["PORT"])
        username = kwargs["USERNAME"]
        password = kwargs["PASSWORD"]
        remote = kwargs["REMOTE"]

        try:
            transport = paramiko.transport.Transport((ip, port))
            transport.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            # Check existence of remote, or raise a exception
            sftp.stat(remote)

            # local IS A DIRECTORY
            if os.path.isdir(local):
                parent_dir = os.path.dirname(local)
                os.chdir(parent_dir)
                target_dir = os.path.basename(local)

                for dirpath, dirnames, filenames in os.walk(target_dir):
                    remote_dir = os.path.join(remote, dirpath)
                    try:
                        sftp.mkdir(remote_dir)
                        self._colored_print(ip, msg_type="success", msg=remote_dir)
                    except IOError:
                        self._colored_print(ip, msg_type="", msg=remote_dir)

                    for filename in filenames:
                        local_file = os.path.join(dirpath, filename)
                        remote_file = os.path.join(remote, local_file)
                        sftp.put(local_file, remote_file)
                        self._colored_print(ip, msg_type="success", msg=remote_file)

            # local IS A PLAIN FILE
            else:
                filename = os.path.basename(local)
                remote_file = os.path.join(remote, filename)
                sftp.put(local, remote_file)
                self._colored_print(ip, msg=remote_file)

        except paramiko.SSHException as err:
            self._colored_print(ip, msg_type="error", msg=str(err))
        except IOError:
            self._colored_print(ip, msg_type="error", msg="remote path does not exist")

    @staticmethod
    def _colored_print(ip, msg_type="success", msg=""):
        pink = '\033[95m'
        blue = '\033[94m'
        green = '\033[92m'
        yellow = '\033[93m'
        red = '\033[91m'
        underline = '\033[4m'
        endc = '\033[0m'

        template = "{0}{1:<15}{2} [ {3} ] {4} "

        if msg_type == "error":
            print(template.format(red, ip, endc, "ERROR", msg))
        else:
            print(template.format(green, ip, endc, "SUCCESS", msg))


if __name__ == "__main__":

    mode = ""
    item = ""

    usage = """
    script -c "command"
    script -t path2file
    script -h
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:t:h")
        if opts:
            for o, a in opts:
                if o == "-c":
                    mode = "command"
                    item = a
                elif o == "-t":
                    mode = "transport"
                    item = a
                else:
                    print(usage)

            ssher = SSHer()
            ssher.execute(mode, item)
        else:
            print(usage)

    except getopt.GetoptError:
        print(usage)
