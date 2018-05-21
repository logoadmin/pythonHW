"""
TCP/IP Server sample

Date: 2018.05.12

傳入socket前須將byte 轉成 byte 
才可進行socket 的 iostream 傳輸

(傳入/寫入socket)   encode():  string ==> byte   
(從socket接收/讀取) decode():  byte   ==> string 

"""
import socket
import pandas as pd

ip = socket.gethostbyname(socket.gethostname())	
HOST = ip
PORT = 5050
url = 'https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9'
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
    table=pd.read_html(url,encoding="big5")[6]
    table = table.drop(table.columns[[0]],axis=0)
    ledn=table[1].values.tolist()
    t=0
    for i in ledn:
        if(i.find(data1)>-1):
            n=t
        t=t+1
    #n=ledn.index(data1)
    number = str(table[1].values.tolist()[n])
    time = str(table[2].values.tolist()[n])
    sell =str(table[3].values.tolist()[n])
    buy =str(table[4].values.tolist()[n])
    sold=str(table[5].values.tolist()[n])
    now =str(table[6].values.tolist()[n])
    high=str(table[10].values.tolist()[n])
    low=str(table[11].values.tolist()[n])
    """
    number = str(table[1].values.tolist()[t])
    time = np.array(table[n:n+1][[2]])
    sell =np.array(table[n:n+1][[3]])
    buy =np.array(table[n:n+1][[4]])
    sold=np.array(table[n:n+1][[5]])
    now =np.array(table[n:n+1][[6]])
    """
    led="股票代號:"+number+" 時間:" +time+" 成交:"+sell+" 買入:"+buy+" 售出:"+sold+" 漲跌:"+now+" 最高:"+high+" 最低:"+low
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
