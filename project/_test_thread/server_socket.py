#! /usr/bin/python

import time
import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print ">> {}".format(data)
        # cur_thread = threading.current_thread()
        # print "Received: {}: {}".format(cur_thread.name, data)
        # response = "{}: {}".format(cur_thread.name, data)
        # self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        # print "Received: {}".format(response)
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9998

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(name="thr_server", target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    try:
        while True:
            print "Main: ", time.ctime(time.time())
            # pass
            # client(ip, port, "Hello World 1")
            # client(ip, port, "Hello World 2")
            # client(ip, port, "Hello World 3")
            time.sleep(3)
    except KeyboardInterrupt:
        print "Server Interrupted"

    print "Shutting down"
    server.shutdown()
    server.server_close()
    print "Bye"
