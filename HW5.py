# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:11:41 2018

@author: X201
"""
import pandas as pd
from pandas import ExcelWriter
import openpyxl
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet.title = "Sheet1"
mon=["Jan.","Feb.","Mar.","Apr.","May","Jun","Jul.","Aug.","Sep.","Oct.","Nov.","Dec."]
row=['(AM9:00)','CO','PM2.5','SO2']
sheet.append(row)
for i in range(2,14):
  sheet["A%d" % (i)].value = mon[i-2]

import csv
arr=[[]for di in range(12)]
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:    
        return False
with open('105_XiTun.csv', newline='') as csvfile:

    rows = csv.DictReader(csvfile)
    #COCOCOCOCCOOCOCOCCOCOOCCOCOCOCCOCOCOCOCOCOCO
    co=0
    CO=[[0]for di in range(1000)] 
    COd=[[]for di in range(1000)]
    cott=[[0]for di in range(13)]
    cot=0.0000000000000000
    cots=0
    #MPMPMPMPMPMPMPMPMPMPMPMPMPMPMPMPMPMPM
    pm=0
    PM=[[0]for di in range(1000)] 
    PMd=[[]for di in range(1000)]
    pmtt=[[0]for di in range(13)]
    pmt=0.0000000000000000
    pmts=0
    #SOSOSOSOSOSSOSOSOSOSOSOSOSOSSOOSOSOSOSOS
    so=0
    SO=[[0]for di in range(1000)] 
    SOd=[[]for di in range(1000)]
    sott=[[0]for di in range(13)]
    sot=0.0000000000000000
    sots=0
    
    
    #CO={'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[]}
    for row in rows:
        x=row['日期'].split("/")
        if(is_float(row['9'])and row['測項']=="CO"):
            CO[co]=float(row['9'])    
            COd[co]=x[1]
            co=co+1
        if(is_float(row['9'])and row['測項']=="PM2.5"):
            PM[pm]=float(row['9'])    
            PMd[pm]=x[1]
            pm=pm+1
        if(is_float(row['9'])and row['測項']=="SO2"):
            SO[so]=float(row['9'])    
            SOd[so]=x[1]
            so=so+1

    for i in range(1,13):
        for xi in range(len(CO)):
            if(COd[xi]==str(i)):
                cot=cot+float(CO[xi])
                cots=cots+1
                #print(i,":",CO[xi]," ",cot,"cots:",cots)  
        cott[i]=str(cot/cots)
        cot=0.00
        cots=0
        
    for i in range(1,13):
        print("CO:",i,":",cott[i])
    for i in range(2,14):
        sheet["B%d" % (i)].value = float(cott[i-1])
        
    for i in range(1,13):
        for xi in range(len(PM)):
            if(PMd[xi]==str(i)):
                pmt=pmt+float(PM[xi])
                pmts=pmts+1
                #print(i,":",PM[xi]," ",pmt,"pmts:",pmts)  
        pmtt[i]=str(pmt/pmts)
        pmt=0.00
        pmts=0
    for i in range(1,13):
        print("PM:",i,":",pmtt[i])
    for i in range(2,14):
        sheet["C%d" % (i)].value = float(pmtt[i-1])
        
    for i in range(1,13):
        for xi in range(len(SO)):
            if(SOd[xi]==str(i)):
                sot=sot+float(SO[xi])
                sots=sots+1
                #print(i,":",SO[xi]," ",sot,"sots:",sots)  
        sott[i]=str(sot/sots)
        sot=0.00
        sots=0
    for i in range(1,13):
        print("SO:",i,":",sott[i])
    for i in range(2,14):
        sheet["D%d" % (i)].value = float(sott[i-1])

    
    wb.save('105_XiTun.xlsx')
    
df1=pd.read_excel('105_XiTun.xlsx', sheetname='Sheet1',skiprows=0)


#開啟要寫入的檔案以及工作表
writer = ExcelWriter('105_XiTun.xlsx')
df1.to_excel(writer,'Sheet1')
workbook = writer.book
worksheet = writer.sheets['Sheet1']
worksheet.conditional_format('A1:E13', {'type': '3_color_scale'})
#畫折線圖
chart = workbook.add_chart({'type': 'line'})

chart.add_series({'name': '=Sheet1!$C$1','categories': '=Sheet1!$B$2:$B$13',
'values': '=Sheet1!$C$2:$C$13'})
chart.add_series({'name': '=Sheet1!$D$1','categories': '=Sheet1!$B$2:$B$13',
'values': '=Sheet1!$D$2:$D$13'})
chart.add_series({'name': '=Sheet1!$E$1','categories': '=Sheet1!$B$2:$B$13',
'values': '=Sheet1!$E$2:$E$13'})

chart.set_x_axis({'name': '月份'})
chart.set_y_axis({'name': '數值', 'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'top'})
worksheet.insert_chart('G2: W20', chart)
writer.save()
    
