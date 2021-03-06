import numpy as np
from pylab import *

# Create some test data
dx = .01
X  = np.loadtxt('dt_submarino.txt')
Y  = exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
#plot(X,Y)
plot(X,CY,'r--')

show()
