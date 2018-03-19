# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:54:32 2018

@author: X201
"""
used =[0,0,0,0]
s=[0,0,0,0]
f=[0,0,0,0]
def bckt(n,list1):
    if(n==4):
        print (s)
    for i in range(0,4):
        if(used[i]==0):
            used[i]=1
            s[n]=f[i]
            bckt(n+1,f)
            used[i]=0

f[0], f[1], f[2] ,f[3] = map(int, input("in:").split())      
bckt(0,f)
                    
    






