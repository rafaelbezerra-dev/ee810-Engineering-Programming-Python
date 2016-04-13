#!/usr/bin/env python

import os, sys
from datetime import datetime
from time import *


OUTPUT_DIR = 'extracted/'
DATETIME_FORMAT = '%Y-%m-%d %X.%f'
CACHE_HIT = 'cache hit'
CACHE_MISS = 'cache miss'

class Reading():
	def __init__(self, str_time, cache_status):
		self.dt = datetime.strptime(str_time, DATETIME_FORMAT)
		self.cache_hit = cache_status == CACHE_HIT
		self.cache_miss = cache_status == CACHE_MISS


def read_from_file(fname):
	lines = []
	with open(fname, 'r+') as f:
		for line in f.readlines():
			str_time, cache_status = line.replace('\n', '').split(', ')
			r = Reading(str_time, cache_status)
			lines.append(r)
	f.close()
	return lines


def write_to_file(fname, content):
	if not os.path.exists(OUTPUT_DIR):
		os.makedirs(OUTPUT_DIR)

	f = open(OUTPUT_DIR + fname, "w+")
	f.write(content + '\n')
	f.close()
	return


def main():
	# dt = datetime.now()
	# sleep(.5)
	# print (datetime.now() - dt).seconds
	# pass
	output = ''
	fname = sys.argv[1]
	readings = read_from_file(fname)
	temp_r = None
	for r in readings:
		if not temp_r:
			temp_r = r
		if temp_r.cache_miss != r.cache_miss:
			if temp_r.cache_miss:
				delta = (r.dt - temp_r.dt).seconds
				output += str(delta) + '\n'
			temp_r = r

	last_reading = readings[len(readings)-1]
	if temp_r.cache_miss == last_reading.cache_miss:
		if temp_r.cache_miss:
			delta = (last_reading.dt - temp_r.dt).seconds
			if delta > 0:
				output += str(delta) + '\n'
	write_to_file(fname, output)





if __name__ == "__main__":	
	main()