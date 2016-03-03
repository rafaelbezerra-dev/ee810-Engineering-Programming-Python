#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('DelayValues.txt')
print len(data)

# Choose how many bins you want here
num_bins = 30

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)

#plt.savefig('plot.png', dpi=150)

plt.show()


