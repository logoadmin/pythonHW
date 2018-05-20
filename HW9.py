# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 07:45:34 2018

@author: Asus1
"""
import pandas as pd
import numpy as np
a = input("input:")
print(a)
url = 'https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.53721000%201523836084'
table=pd.read_html(url,encoding="big5")[6]
table = table.drop(table.columns[[0]],axis=0)
#print(table)
#led = np.array(table[2][[1,2,3,4,5,6,7,9,10,11]])
ledn=table[1].values.tolist()
t=0
for i in ledn:
    if(i.find(a)>-1):
        n=t
    t=t+1
#n=ledn.index(a)
number = np.array(table[n:n+1][[1]])
time = np.array(table[n:n+1][[2]])
sell =np.array(table[n:n+1][[3]])
buy =np.array(table[n:n+1][[4]])
sold=np.array(table[n:n+1][[5]])
now =np.array(table[n:n+1][[6]])
led="股票代號:"+number+" 時間:" +time+" 成交:"+sell+" 買入:"+buy+" 售出:"+sold+" 漲跌"+now
print(led)

     
