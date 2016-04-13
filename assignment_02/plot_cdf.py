#!/usr/bin/env python

import os, sys
import numpy as np
import matplotlib.pyplot as plt

def main():
	src = str(sys.argv[1])
	dest = str(sys.argv[2])

	data = np.loadtxt(src)
	sorted_data = np.sort(data)
	yvals=np.arange(len(sorted_data))/float(len(sorted_data))

	plt.title(src[:src.rfind('.')].upper())
	plt.plot(sorted_data,yvals)
	plt.savefig(dest)


if __name__ == "__main__":	
	main()