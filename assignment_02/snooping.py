#!/usr/bin/env python

# python snooping.py google.com cnn.com g1.globo.com www.r7.com jovemnerd.com.br 9gag.com www.submarino.com.br reddit.com stackoverflow.com

import sys, os, time, threading
from datetime import datetime

DELAY = 5
DOM_PREFIX = 'www.'
CACHE_HIT = 'cache hit'
CACHE_MISS = 'cache miss'

def dig(domain):
	import subprocess
	# dig +nocmd +noall +answer +norecurse www.r7.com	
	command = 'dig +nocmd +noall +answer +norecurse ' + domain
	# print command
	p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	ans = p.communicate()[0]
	# print ans
	return ans

def append_to_file(fname, content):
	f = open(fname, "a")
	f.write(content + '\n')
	f.close()
	return


def run_dig(domain, run_event):
	while run_event.is_set():		
		ans = dig(domain)	
		fname = domain.replace(DOM_PREFIX, '') + '.txt'
		now = str(datetime.now())
		content = ''
		if not ans:
			content = now + ', ' + CACHE_MISS
			print now, domain, CACHE_MISS
		else:
			content = now + ', ' + CACHE_HIT
			print now, domain, CACHE_HIT
		append_to_file(fname, content)
		time.sleep(DELAY)

def main():	
	run_event = threading.Event()
	run_event.set()
	threads = []
	param = sys.argv[1]
	if param == '-d':
		for arg in sys.argv[2:]:
			# if not arg.startswith(DOM_PREFIX):
			# 	arg = DOM_PREFIX + arg
			print 'Starting thread for ', arg
			tr = threading.Thread(target = run_dig, args = (arg, run_event))
			threads.append(tr)
			tr.start()
	elif param == '-f':
		with open(sys.argv[2], 'r') as f:
			for line in f.readlines():
				line = line.replace('\n','')
				if line:
					print 'Starting thread for ', line
					tr = threading.Thread(target = run_dig, args = (line, run_event))
					threads.append(tr)
					tr.start()
		f.close()

	try:
		while 1:
			pass
	except KeyboardInterrupt:
		print "attempting to close threads"
		run_event.clear()
		for tr in threads:
			tr.join()
		print "threads successfully closed"

if __name__ == "__main__":	
	main();