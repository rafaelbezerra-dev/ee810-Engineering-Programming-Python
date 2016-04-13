#!/usr/bin/env python

import os, sys
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = 'cdf/'

def main():
	src = str(sys.argv[1])
	dest = OUTPUT_DIR + src

	data = np.loadtxt(src)
	sorted_data = np.sort(data)
	yvals=np.arange(len(sorted_data))/float(len(sorted_data))

	plt.title(src[:src.rfind('.')].upper())
	plt.plot(sorted_data,yvals)

	if not os.path.exists(OUTPUT_DIR):
		os.makedirs(OUTPUT_DIR)

	plt.savefig(dest)


if __name__ == "__main__":	
	main()