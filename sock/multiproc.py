from multiprocessing import Process

import os
import time


def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):
        print('parent process: {}'.format(os.getppid()))
    print('process id: {}'.format(os.getpid()))


def f(name):
    info('function f')
    time.sleep(2)
    print('hello {}'.format(name))


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
