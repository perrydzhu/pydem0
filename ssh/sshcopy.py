import sys
import os.path
import paramiko


if len(sys.argv) != 5:
    print("Usage: python {0} host username password src-file".format(sys.argv[0]))
    sys.exit(-1)

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
src = sys.argv[4]
filename = os.path.basename(src)

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, port=22, username=username, password=password)
    sftp = client.open_sftp()
    sftp.put(src, os.path.join("/tmp", filename))

except Exception as e:
    print(e)
    print("Error happened when copying file to {0}".format(host))
    sys.exit(-1)

