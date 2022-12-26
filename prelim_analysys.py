import csv
import matplotlib.pyplot as plt
import numpy as np

array = []
with open('/home/harsh/Downloads/Jan-March.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        #print(lines)
        array.append(float(lines[0]))

#print(array)
Ts=1
tau = 2000
a = Ts/(2*tau+Ts)
b=(2*tau-Ts)/(2*tau+Ts)
out=[0]*len(array)
for i in range(len(array)):
  if(i<1):
    pre_in=0
    pre_out=0
  else:
    pre_in=array[i-1]
    pre_out=out[i-1]

  out[i]=a*(array[i]+pre_in) + b*pre_out


plt.plot(array)
plt.plot(out)
plt.plot(np.subtract(np.array(array),np.array(out)))
plt.show()