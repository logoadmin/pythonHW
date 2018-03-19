# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:33:10 2018

@author: MSIZ77
"""

s=input("in:").split()
x=""
for j in range (0,len(s)):
    T=list(s[j])
    a=[None]*len(T)
    for i in range (1,len(T)-1):
        a[len(T)-1-i]=T[i]
    a[0]=T[0]
    a[len(T)-1]=T[len(T)-1]
    #for i in range (0,len(a)-1):
    #    if(a[i]==" "):
    #        del a[i]
    str="".join(a)
    x=x+str
    
print(x)
    
