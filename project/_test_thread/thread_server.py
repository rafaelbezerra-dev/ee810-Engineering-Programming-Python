#! /usr/bin/python

import threading
import socket
import time

HOST = ""                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

def connectionHandler():
    print "handler >> creating socket"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "handler >> binding to port", PORT
    s.bind((HOST, PORT))
    s.setblocking(1 )
    print "handler >> listening"
    s.listen(1)
    print "handler >> heard something"
    conn, addr = s.accept()
    print "Connected by", addr
    while True:
        data = conn.recv(1024)
        print ">> ", data
        # if not data: break
        # conn.sendall(data)
    conn.close()

if __name__ == "__main__":
    print "Initializing connection handler"
    conn_hdlr = threading.Thread(name="thr_connection_handler", target=connectionHandler)
    conn_hdlr.start()

    while True:
        print time.ctime(time.time())
        time.sleep(2)
