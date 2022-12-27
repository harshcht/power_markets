from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ar=pd.read_csv('data_Jan-Nov.csv')

print(ar.head())

result = seasonal_decompose(ar['prices'], 
                            model ='multiplicative',period=96*7)


result.plot()
plt.show()