import os.path
import subprocess
from flask import Flask, redirect


ISO_PATH = '/opt/isos'
BASE_MOUNT_PATH = '/mirrors'


app = Flask(__name__)


@app.route('/')
def default():
    return redirect("http://127.0.0.1")


@app.route('/<path:query>/')
def automount(query):
    print(query)
    iso = query.split('/')[0]
    mount_path = os.path.join(BASE_MOUNT_PATH, iso)
    iso2mount = os.path.join(ISO_PATH, iso)

    if not os.path.exists(mount_path):
        print("not exists, create")
        ret = subprocess.call('/bin/mkdir {}'.format(mount_path), shell=True)
        print(ret)

    command = '/bin/mount -o loop {} {}'.format(iso2mount, mount_path)
    print(command)
    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print('PID: {}'.format(proc.pid))

    return redirect("http://127.0.0.1/{}".format(query))


if __name__ == '__main__':
    app.run()
