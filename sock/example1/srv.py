#!/usr/bin/env python

import socket,time

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)
print "Server listening:", s.getsockname()

while True:
    conn, addr = s.accept()
    print "Accept client:", conn.getpeername()
    
    while True:
        try:
            data = conn.recv(1024).strip()
            if (not data) or (data.upper() == "QUIT"):
                print "Client quit"
                break
            
            if data.upper() == "DATE":
                ret = time.strftime("%Y-%m-%d",time.gmtime()) 
                conn.sendall(ret)
            else:
                ret = "[ ECHO ]: "+ data
                conn.sendall(ret)

        except socket.error:
            print "Bye,",conn.getsockname()
            break
