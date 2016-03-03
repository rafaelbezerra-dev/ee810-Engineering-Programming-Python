import numpy as np
import matplotlib.pyplot as plt

# some fake data
#data = np.random.randn(1000)
data = np.loadtxt('DelayValues.txt')
print len(data)
# evaluate the histogram
values, base = np.histogram(data, bins=40)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue')

plt.show()