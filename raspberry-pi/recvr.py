from socket import *
import json

DEFAULT_PORT = 8888

def send(ip, port, message):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((ip, port))
	try:
		sock.sendall(message)
		response = sock.recv(1024)
		return
		# print "Received: {}".format(response)
	finally:
		sock.close()

def main():
	s=socket(AF_INET, SOCK_DGRAM)
	s.bind(('',DEFAULT_PORT))
	data=s.recvfrom(1024)

	# print 'Data recieved', str(data[0])
	server = json.loads(data[0])

	print "Hi from Raspberry Pi\n"
	print "My address is " 
	print server['host']
	print "Come talk to me!\n"

	send(server['host'], server['port'], 'close')


	return;

if __name__ == "__main__":
	main()



