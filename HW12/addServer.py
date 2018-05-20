"""
TCP/IP Server sample

Author: Gwo-Chuan Lee 
Date: 2018.05.12

傳入socket前須將byte 轉成 byte 
才可進行socket 的 iostream 傳輸

(傳入/寫入socket)   encode():  string ==> byte   
(從socket接收/讀取) decode():  byte   ==> string 

"""
import numpy as np
import socket
import pandas as pd
HOST = '192.168.1.113'
PORT = 5050
url = 'https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.53721000%201523836084'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#繫結socket
server.bind((HOST, PORT))
#開始監聽用戶端連接
server.listen(1)
print('Listening at port:',PORT)

while True: # 伺服器需不斷的測試是否有Client與之相連
    
	#取得與客戶端連結的位址 addr 與 Socket物件 connect_client
    connect_client, addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
	
	#讀取客戶端的資料, 並使用 decode() 將 byte 轉成 string
    data1 = connect_client.recv(1024).decode()
	#data2 = connect_client.recv(1024).decode()
    	#data=int(data1)+int(data2)
    #print('Received: %s + %s = %d'%(data1,data2,data))
    table=pd.read_html(url,encoding="big5")[6]
    table = table.drop(table.columns[[0]],axis=0)
    ledn=table[1].values.tolist()
    t=0
    for i in ledn:
        if(i.find(data1)>-1):
            n=t
        t=t+1
    #n=ledn.index(data1)
    number = np.array(table[n:n+1][[1]])
    time = np.array(table[n:n+1][[2]])
    sell =np.array(table[n:n+1][[3]])
    buy =np.array(table[n:n+1][[4]])
    sold=np.array(table[n:n+1][[5]])
    now =np.array(table[n:n+1][[6]])
    led="股票代號:"+number+" 時間:" +time+" 成交:"+sell+" 買入:"+buy+" 售出:"+sold+" 漲跌:"+now
    print(led)
    """
    table = table[[1,2,3,4,5,6,7,9,10,11]]
    data=table[4]
    #print(table)
    led = np.array(table[2:3][[1,2,3,4,5,6,7,9,10,11]])
    print(led)
    """


	#傳送資料到客戶端
	#傳入socket前須先使用 encode()將 string 轉成 byte 以利 iostream 傳輸
    #若不轉換成 byte 將造成錯誤
    connect_client.send(str(led).encode())
    connect_client.close()

#server.close()
