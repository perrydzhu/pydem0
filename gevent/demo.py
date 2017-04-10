from gevent import monkey
monkey.patch_all()

import time
import random
import gevent
from ssh_cmd import SSHCmd


def echo(host):
    print('Processing: {}'.format(host))
    words = ['hi', 'apple', 'hello', 'good']
    cmd = 'sh /root/echo.sh {}'.format(random.choice(words))
    ssh = SSHCmd('root', 'hello', host)
    ssh.execute(cmd)


if __name__ == '__main__':
    start = time.time()

    ip = ['10.0.0.117', '10.0.0.107', '10.0.0.107', '10.0.0.117', '10.0.0.107', '10.0.0.117']
    threads = []
    for host in ip:
        threads.append(gevent.spawn(echo, host))
    gevent.joinall(threads)

    end = time.time() - start

    print("Elapse: {}".format(end))
