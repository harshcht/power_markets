from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf


ar=pd.read_csv('/home/harsh/Documents/combined_data.csv')


print(ar.head())

result = seasonal_decompose(ar['prices'], 
                            model ='multiplicative',period=96)

                            
plot_acf(ar['prices'],lags=10000)
plt.show()
#result.plot()
#plt.show()