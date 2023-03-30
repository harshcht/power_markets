import numpy as np

# Define two time series
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Compute the cross-correlation using the numpy.correlate function
corr = np.correlate(x, y, mode='full')

# Compute the lags for the cross-correlation
lags = np.arange(-len(x)+1, len(y))

# Plot the cross-correlation function
import matplotlib.pyplot as plt
plt.stem(lags, corr)
plt.xlabel('Lag')
plt.ylabel('Cross-correlation')
plt.show()