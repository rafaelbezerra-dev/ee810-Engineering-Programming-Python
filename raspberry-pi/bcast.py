# netcat -lu -p 8888
import sys, time
import threading, json
from socket import *
from Queue import *

DEFAULT_PORT = 8888

class Server:
	def __init__(self, host='', port=0):
		self.host = host
		self.port = port
		return

def listener(lstr, result_queue):
	print "listener >> creating socket"
	s = socket(AF_INET, SOCK_STREAM)
	try:
		print "listener >> binding to port", lstr.port
		s.bind((lstr.host, lstr.port))
		s.setblocking(1)
		print "listener >> listening"
		s.listen(1)
		print "listener >> heard something"
		conn, addr = s.accept()
		try:
			print "Connected by", addr
			while True:
				data = conn.recv(1024)
				if data == 'close':
					print data
					result_queue.put('done')
					break
		finally:
			print "closing connection"
			conn.close()
	finally:
		print "closing listener socket"
		s.close()
	return



def main():
	print "retrieving local ip address"	
	s = socket(AF_INET, SOCK_DGRAM)
	try:
		s.connect(("gmail.com", 80))
		local_ip_addr = s.getsockname()[0]
		s.close()

		print "Initializing connection listener"
		lstr = Server('', DEFAULT_PORT + 3)
		q = Queue()
		conn_hdlr = threading.Thread(name="thr_listener", target=listener, args=[lstr, q])
		conn_hdlr.start()

		s = socket(AF_INET, SOCK_DGRAM)
		s.bind(('', 0))
		s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

		pi_host = Server(local_ip_addr, lstr.port)

		for x in range(0, 3000):
			data = json.dumps(pi_host.__dict__)
			print data
			s.sendto(data, ('<broadcast>', DEFAULT_PORT))
			if not q.empty():
				data = q.get(True, 2)
				if data:
					break
			else:
				time.sleep(2)
	finally:
		print "closing main socket"
		s.close()
	return

if __name__ == "__main__":
	main()
