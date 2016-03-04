#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

source = 'dt_unesp.txt'
def plot1(src):
    data = np.loadtxt(src)
    sorted_data = np.sort(data)
    cumulative = np.cumsum(sorted_data)
    plt.plot(sorted_data, np.linspace(0,1,sorted_data.size))

def plot2(src):
    data = np.loadtxt(src)
    sorted_data = np.sort(data)
    yvals=np.arange(len(sorted_data))/float(len(sorted_data))

    plt.plot(sorted_data,yvals)


# plot1('dt_github.txt')
# plot1('dt_infnet.txt')
# plot1('dt_jovemnerd.txt')
# plot1('dt_submarino.txt')
plot1('dt_unesp.txt')

# plot2('dt_github.txt')
# plot2('dt_infnet.txt')
# plot2('dt_jovemnerd.txt')
# plot2('dt_submarino.txt')
plot2('dt_unesp.txt')
plt.show()
