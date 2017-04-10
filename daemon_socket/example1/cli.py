#!/usr/bin/env python

import socket,time

HOST = "127.0.0.1"
#HOST = "192.168.110.134"
PORT = 10086

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
    msg = raw_input('>')

    if not msg:
        break

    s.send(msg)

    if msg.upper() == "QUIT":
        break

    data = s.recv(1024)
    if not data:
        break

    print data

