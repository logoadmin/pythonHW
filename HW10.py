
import pandas as pd

#data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
data=pd.read_csv("http://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv")
dataf=pd.DataFrame(data)
l=[]
v=[]
c=[]
i=0
print("良好")
for row in dataf.ix[:, 'AQI']:   
    if(row>0 and row<=50 and dataf.ix[i, 'County'] not in l ):
        l.append(dataf.ix[i, 'County'])
        print(dataf.ix[i, 'County'])
    i=i+1
j=0
print("普通")
for row in dataf.ix[:, 'AQI']:        
    if(row>50 and row<=100 and dataf.ix[j, 'County'] not in v):
        v.append(dataf.ix[j, 'County'])
        print(dataf.ix[j, 'County'])
    j=j+1
k=0 
print("不良")   
for row in dataf.ix[:, 'AQI']:        
    if(row>100 and dataf.ix[k, 'County'] not in c):
        c.append(dataf.ix[k, 'County'])
        print(dataf.ix[k, 'County'])
    k=k+1
#print(dataf.ix[:, 'AQI'])
#print(data)