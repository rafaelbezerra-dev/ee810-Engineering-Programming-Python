#! /usr/bin/python

# Echo client program
import socket, sys

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
PORT = 9997              # The same port as used by the server

HOST = sys.argv[1]
PORT = int(sys.argv[2])
# print HOST, PORT
# send(HOST, PORT, "Hello World 1")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))

while True:
    msg = raw_input('>> ')
    send(HOST, PORT, msg)
    if msg == "/quit" or msg == "/q":
        break
# s.sendall('Hello, world')
# data = s.recv(1024)
# print 'closing'
# s.close()
print 'bye'
# print 'Received', repr(data)
