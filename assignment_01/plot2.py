import sys, os
import numpy as np
import matplotlib.pyplot as plt

source = str(sys.argv[1])
# some fake data
#data = np.random.randn(1000)
data = np.loadtxt(source)
print len(data)
# evaluate the histogram
values, base = np.histogram(data, bins=50)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue')

plt.show()
