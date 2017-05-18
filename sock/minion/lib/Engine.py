import os
import re
import time
import glob
import time
import socket
import subprocess

from Logger import *

class Engine:
    def __init__(self):
        self.logger = Logger()

    def start(self,sock):
        (peerIP,peerPort) = sock.getpeername()

        while True:
            # Receive message from boss
            try:
                msg = sock.recv(1024).strip()
                self.logger.log("DEBUG","Boss said: {0}".format(msg))



                if msg.upper() == "BYE":
                    sock.sendall("[echo]:Bye")
                    sock.close()


                sock.sendall("[echo]:{0}".format(msg))
            except socket.error:
                self.logger.log("INFO","Bye! Master({0}:{1})".format(peerIP,peerPort))
                sock.close()
                break


    
    
