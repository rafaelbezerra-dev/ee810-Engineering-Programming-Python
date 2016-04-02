#! /usr/bin/python

# Echo server program
import sys, socket

HOST = sys.argv[1]#''                 # Symbolic name meaning all available interfaces
PORT = sys.argv[2]#50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
