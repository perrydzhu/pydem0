import sys
import paramiko


if len(sys.argv) != 5:
    print("Usage: python {0} host username password command".format(sys.argv[0]))
    sys.exit(-1)

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())
    print(stderr.read())
except Exception as e:
    print(e)
    print("Error happened when invoking script on {0}".format(host))
    sys.exit(-1)
