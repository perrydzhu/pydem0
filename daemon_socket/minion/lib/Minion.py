###### AUTHOR           Skipper.D
###### DESCRIPTION      A daemon module_package
###### VERSION          v1.1
###### UPDATE           2015/11/20
###### PYTHON VERSION   2
import os
import sys
import time
import atexit
from signal import SIGTERM

from MSock import *
from Logger import *


class Minion:
    def __init__(self,logPath,host,port):
        DIR_NAME = logPath
        LOG = DIR_NAME+"/minion.log"
        PID_FILE = DIR_NAME+"/minion.pid"

        # Redirect /dev/null to stdin
        self.stdin = "/dev/null"
        # Redirect stdout,stderr to LOG
        self.stdout = LOG
        self.stderr = LOG

        self.pidfile = PID_FILE
        self.host = host
        self.port = port

        # Setup a logger
        self.logger = Logger()
    
    def _daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
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
        newin = file(self.stdin,'r')
        newout = file(self.stdout,'a+')
        newerr = file(self.stderr,'a',0)
        # redirect stdin,stdout,stderr
        os.dup2(newin.fileno(), sys.stdin.fileno())
        os.dup2(newout.fileno(), sys.stdout.fileno())
        os.dup2(newerr.fileno(), sys.stderr.fileno())

        atexit.register(self._delete_pid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write(pid+"\n")

    def _delete_pid(self):
        os.remove(self.pidfile)



    
    ###############################
    ######   Public method   ######
    ###############################
    def work(self):
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        
        if pid:
            msg = "Robot(PID: {0}) already working\n".format(pid)
            sys.stderr.write(msg)
            sys.exit(1)

        self._daemonize()
        self.logger.log("INFO","Robot worked")

        sock = MSock(self.host,self.port)
        sock.plug()

    def rest(self):
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()

            if pid:
                os.kill(pid, SIGTERM)
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                return
        except IOError:
            print "Robot not wroking"
