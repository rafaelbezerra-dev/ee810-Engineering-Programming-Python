#!/usr/bin/env python

import os, sys
from datetime import datetime
from time import *

DATETIME_FORMAT = '%Y-%m-%d %X.%f'
CACHE_HIT = 'cache hit'
CACHE_MISS = 'cache miss'

class Reading():
	def __init__(self, str_time, cache_status):
		self.dt = datetime.strptime(str_time, DATETIME_FORMAT)
		self.cache_hit = cache_status == CACHE_HIT
		self.cache_miss = cache_status == CACHE_MISS


def read(fname):
	lines = []
	with open(fname, 'r+') as f:
		for line in f.readlines():
			str_time, cache_status = line.split(', ')
			r = Reading(str_time, cache_status)
	f.close()
	return lines

def main():
	# dt = datetime.now()
	# sleep(.5)
	# print (datetime.now() - dt).seconds
	# pass
	readings = read(sys.argv[1])
	temp_r = None
	for r in readings:
		if not temp_r:
			temp_r = r
		if temp_r.cache_miss == r.cache_miss:
			



if __name__ == "__main__":	
	main()