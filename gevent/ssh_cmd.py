from __future__ import print_function
import sys
import time
import socket
import argparse
import gevent
import paramiko


class SSHCmd(object):
    def __init__(self, username, password, host, port=22, timeout=60):
        self._username = username
        self._password = password
        self._host = host
        self._port = port
        self._timeout = timeout
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute(self, *command):
        try:
            self._ssh.connect(self._host, self._port, self._username, self._password, timeout=self._timeout, look_for_keys=False)
            gevent.sleep(0)
            for cmd in command:
                _, stdout, stderr = self._ssh.exec_command(cmd)

                for line in stdout:
                    print(line, end='')

                for line in stderr:
                    print(line, end='')

        except paramiko.SSHException as err:
            print('[paramiko.SSHException]: {}'.format(err))
        except socket.error as err:
            print('[socket.error]: {}'.format(err))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='Specify the user to login')
    parser.add_argument('-p', '--password', required=True, help='Specify the password to login')
    parser.add_argument('-H', '--hostname', required=True, help='Specify the hostname/IP')
    parser.add_argument('-P', '--port', default=22, type=int, help='Specify the ssh port')
    parser.add_argument('cmd', type=str, help='Specify the command to execute')
    args = parser.parse_args()
    ssh = SSHCmd(args.username, args.password, args.hostname, port=args.port)
    ssh.execute(args.cmd)

if __name__ == '__main__':
    main()
