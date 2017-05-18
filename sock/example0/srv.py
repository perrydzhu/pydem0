#!/usr/bin/env python

import socket,sys,time


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
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
sock.bind((HOST,PORT))
sock.listen(1)

while True:
    print "Listening at", sock.getsockname()
    cli,sockname =sock.accept()
    print "Accepted a connection from",sockname
    print "Socket connects",cli.getsockname(), "and", cli.getpeername()
    message = recv_all(cli,16)
    print "The incoming 16-octet message says", repr(message)
    time.sleep(5)
    cli.sendall("Farewell, client")
    cli.close()
    print "Reply sent, socket closed"

