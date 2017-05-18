###### AUTHOR           Skipper.D
###### DESCRIPTION      A Socket module_class
###### VERSION          v1.1
###### UPDATE           2015/11/20
###### PYTHON VERSION   2
import os
import sys
import socket
from threading import Thread
from multiprocessing import Process

from Logger import *
from Engine import *


class MSock:
    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = Logger()
        self.engine= Engine()

    def plug(self):
        self.srv.bind((self.HOST,self.PORT))
        self.srv.listen(5)
        (sockIP,sockPort) = self.srv.getsockname()
        self.logger.log("INFO","Minion Listening: {0}:{1}".format(sockIP,sockPort))

        while True:
            peer,addr = self.srv.accept()
            (peerIP,peerPort) = peer.getpeername()
            self.logger.log("INFO","Boss({0}:{1}) Connected".format(peerIP,peerPort))

            t = Thread(target=self.engine.start,args=(peer,))
            #t = Process(target=self.engine.start,args=(peer,))
            t.start()

