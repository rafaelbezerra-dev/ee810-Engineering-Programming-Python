MYPORT = 9999
# netcat -lu -p 9999
import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
	data = repr(time.time()) + '\n'
	print 'sending: ', data
	s.sendto(data, ('<broadcast>', MYPORT))
	time.sleep(2)
