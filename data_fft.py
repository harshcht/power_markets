import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
import scipy

array = []
with open('/home/harsh/Documents/2021.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        #print(lines)
        array.append(float(lines[0]))

arr=fft(array)
print(arr)
print(len(arr))
ns=np.array([i for i in range(len(arr))])
plt.scatter(ns,abs(arr))

plt.show()