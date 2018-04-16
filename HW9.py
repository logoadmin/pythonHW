# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 07:45:34 2018

@author: Asus1
"""
import pandas as pd


url = 'https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.53721000%201523836084'
table=pd.read_html(url)[6]
table = table.drop(table.columns[[0]],axis=0)
table = table[[1,2,3,4,5,6,7,9,10,11]]
print(table)

     
