#!/usr/bin/env python

import socket, sys


def recv_all(sock, length):
    data = ""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("socket closed %d bytes into a %d-byte message" % (len(data), length))
        data += more
    return data

HOST = "127.0.0.1"
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
print "Client has been assigned socket name", sock.getsockname()
sock.sendall("Hi there, server!")
reply = recv_all(sock,16)
print "The server said", repr(reply)
sock.close()

