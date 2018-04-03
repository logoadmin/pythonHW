from pandas import DataFrame,Series  
import pandas_datareader as pdr
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

def moving_average(a, n) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

c=[]
c30=[]
c60=[]
c90=[]
start=datetime.datetime(2016,8,25)
end=datetime.date.today()
data=pdr.get_data_yahoo('2454.tw',start,end) 

for row in data['close']:
    c.append(row)
    
c30=moving_average(c, 30)
c60=moving_average(c, 60)
c90=moving_average(c, 90)
cc90=[]
cc30=[]
cc60=[]
cc=[]
for i in range (0,301):
    cc30.append(c30[i])
    cc60.append(c60[i])
    cc.append(c[i])
    cc90.append(c90[i])


dataa = {"1day":cc, "30days":cc30, "60days":cc60, "90days":cc90} 
f1 = DataFrame(dataa) 
print (f1)
f1.plot()
plt.title("2454.tw Mediatek")
plt.xlabel("Days to today")
plt.ylabel("Price")
plt.gca().invert_xaxis() 
plt.show()
