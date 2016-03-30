#! /usr/bin/python

# Echo client program
import socket

def send(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        # print "Received: {}".format(response)
    finally:
        sock.close()

HOST = 'localhost'    # The remote host
PORT = 9998              # The same port as used by the server

# send(HOST, PORT, "Hello World 1")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
msg = raw_input('>> ')
while msg.lower() != "\quit" or msg.lower() != "\q":
    send(HOST, PORT, msg)
    msg = raw_input('>> ')
send(HOST, PORT, "\q")
# s.sendall('Hello, world')
# data = s.recv(1024)
# print 'closing'
# s.close()
# print 'bye'
# print 'Received', repr(data)
