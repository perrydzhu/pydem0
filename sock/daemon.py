#!/usr/bin/env python

import sys
import os
import socket
import time
import atexit
from signal import SIGTERM


class Sock:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def on(self):
        self.s.bind((self.host, self.port))
        self.s.listen(1)

        print "Server Listenning:", self.s.getsockname()

        while True:
            cli, addr = self.s.accept()
            client = cli.getpeername()
            print client, "Connected"

            while True:
                data = cli.recv(1024).strip()
                if (not data) or (data.upper() == "QUIT"):
                    print client, "Quit"
                    break

                if data.upper() == "DATE":
                    ret = time.strftime("%Y-%m-%d", time.gmtime())
                    cli.sendall(ret)
                else:
                    ret = "[ECHO]:" + data
                    cli.sendall(ret)


class Daemon:
    def __init__(self):
        file_path = os.path.realpath(__file__)
        dir_name = os.path.dirname(file_path)
        LOG = dir_name + "/main.log"
        PID_FILE = dir_name + "/daemon_socket.pid"

        self.stdin = "/dev/null"
        self.stdout = LOG
        self.stderr = LOG
        self.pidfile = PID_FILE

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0: sys.exit(0)
        except OSError:
            sys.stderr.write("Fork #1 failed :/\n")
            sys.exit(1)
        os.setsid()
        os.chdir("/")
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0: sys.exit(0)
        except OSError:
            sys.stderr.write("Fork #2 failed :/\n")
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()
        newin = file(self.stdin, 'r')
        newout = file(self.stdout, 'a+')
        newerr = file(self.stderr, 'a', 0)
        # redirect stdin,stdout,stderr
        os.dup2(newin.fileno(), sys.stdin.fileno())
        os.dup2(newout.fileno(), sys.stdout.fileno())
        os.dup2(newerr.fileno(), sys.stderr.fileno())

        atexit.register(self.delete_pid)
        pid = str(os.getpid())
        file(self.pidfile, 'w+').write(pid + "\n")

    def delete_pid(self):
        os.remove(self.pidfile)

    def start(self):
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            msg = "Daemon(PID: %d) is running\n"
            sys.stderr.write(msg % pid)
            sys.exit(1)
        self.daemonize()

        sys.stdout.write("[ INFO ]: Daemon Started\n")

        ################################
        ###### Function goes here ######
        ################################
        self.foo()

    def stop(self):
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:

            os.kill(pid, SIGTERM)
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)
        else:
            return

    def foo(self):
        # while True:
        #    sys.stdout.write("hi\n")
        #    time.sleep(5)

        sock = Sock("192.168.110.134", 8888)
        sock.on()


if __name__ == "__main__":
    daemon = Daemon()

    if len(sys.argv) == 2:
        if sys.argv[1] == "on":
            print "Daemon ON ..."
            daemon.start()
        elif sys.argv[1] == "off":
            print "Daemon OFF ..."
            daemon.stop()
        else:
            print "Usage: %s on|off" % sys.argv[0]
            sys.exit(2)
    else:
        print "Usage: %s on|off" % sys.argv[0]
        sys.exit(2)
