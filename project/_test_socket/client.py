#! /usr/bin/python

# Echo client program
import sys, socket

HOST = sys.argv[1]#'localhost'    # The remote host
PORT = sys.argv[2]#50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
person = input('>> ')
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
