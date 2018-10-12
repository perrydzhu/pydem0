import sys
import paramiko


param = len(sys.argv)
background = False

if param < 5:
    print("Usage: python {0} host username password command <bg>".format(sys.argv[0]))
    sys.exit(-1)
if param == 6:
    background = True

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, port=22, username=username, password=password)
    if background:
        transport = client.get_transport()
        channel = transport.open_session()
        channel.exec_command(command)
        print("Run command '{0}' in background on remote host {1}".format(command, host))
    else:
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read())
        print(stderr.read())
except Exception as e:
    print(e)
    print("Error happened when invoking script on {0}".format(host))
    sys.exit(-1)
