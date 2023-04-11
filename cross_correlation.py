import numpy as np
import csv
from ast import literal_eval

nci=[]
dam_prices=[]
with open('nci_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        #print(', '.join(row))
        nci.append(literal_eval(row[0]))
        dam_prices.append(literal_eval(row[1]))
# Define two time series
#x = np.array([1, 2, 3, 4, 5])
#y = np.array([-10, 1, 2, 3, 4])
#print(nci)
#print(np.array(nci))
# Compute the cross-correlation using the numpy.correlate function
corr = np.correlate(np.array(nci), np.array(dam_prices), mode='full')
print(len(nci))
print(len(dam_prices))
# Compute the lags for the cross-correlation
lags = np.arange(-len(nci)+1, len(dam_prices))

# Plot the cross-correlation function
import matplotlib.pyplot as plt
plt.plot(lags, corr)
plt.xlabel('Lag')
plt.ylabel('Cross-correlation')
plt.show()