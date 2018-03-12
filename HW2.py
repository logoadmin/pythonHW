# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:40:16 2018

@author: X201
"""

list=[30,98,12,191,66,47,82,54]
for i in range (0,len(list)-1):
    min=i
    for l in range(i+1,len(list)):
        if list[l]<list[min]:
            min=l
    if min!=i:
        temp=list[i]
        list[i]=list[min]
        list[min]=temp
    
print("list:",list)            
            