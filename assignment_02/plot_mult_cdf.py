#!/usr/bin/env python

import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D


OUTPUT_DIR = 'cdf/'
COLORS = [
	# 'yellow',
	'magenta',
	'cyan',
	'red',
	'green',
	'blue',
	# 'white',
	'black'
]

def main():
	# line1, = plt.plot([3,2,1], marker='o', label='Line 1')
	# line2, = plt.plot([1,2,3], marker='o', label='Line 2')

	# return

	dest = OUTPUT_DIR + sys.argv[1].replace('.txt', '.png')

	if '.png' not in dest:
		dest += '.png'
	line1 = None
	handles = []
	color_count = 0
	for src in sys.argv[2:]:		
		print 'ploting ' + src
		color = COLORS[color_count % len(COLORS)]
		color_count += 1

		data = np.loadtxt(src)
		sorted_data = np.sort(data)
		yvals=np.arange(len(sorted_data))/float(len(sorted_data))

		# plt.title(src[:src.rfind('.')].upper())
		line, = plt.plot(sorted_data,yvals, color=color, label=src.replace('.txt', ''))
		if not line1:
			line1 = line

	if not os.path.exists(OUTPUT_DIR):
		os.makedirs(OUTPUT_DIR)
	
	plt.xlabel('Seconds')
	plt.ylabel('Probability')
	plt.title('CDF for Measured Cache Gap')
	plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)}, loc=4)
	plt.show()
	# plt.savefig(dest)


if __name__ == "__main__":	
	main()