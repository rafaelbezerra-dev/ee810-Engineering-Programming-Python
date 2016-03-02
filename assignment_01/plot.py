#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('DelayValues.txt')

# Choose how many bins you want here
num_bins = 20

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)

plt.savefig('plot.png', dpi=150)

#plt.show()


