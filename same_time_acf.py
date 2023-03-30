import csv
import matplotlib.pyplot as plt
import numpy as np
from pmdarima import auto_arima
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose



array = []
with open('/home/harsh/Documents/combined_data.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        #print(lines)
        array.append(float(lines[0]))
def getPt(index,list,n):
    i=index
    new_Arr=[]
    while(i < len(list)):
        new_Arr.append(list[i])
        i+=n

    return new_Arr

pt_Arr=(getPt(0,array,1))
pt2=getPt(0,pt_Arr,96)
pt_df=pd.DataFrame(pt_Arr,columns=['bifurcated'])
pt2df=pd.DataFrame(pt2,columns=['same_day'])
#print(pt_df.head())
#print(pt_df['bifurcated'].tolist())
#plot_acf(pt2df['same_day'],lags=698)
result = seasonal_decompose(pt_df['bifurcated'], 
                            model ='additive',period=96)
result.plot()
#print(result.resid[48:67054])
#plot_acf(result.resid[182:66920],lags=698)
plt.show()