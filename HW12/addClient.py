"""
TCP/IP Client Server sample

Author: Gwo-Chuan Lee 
Date: 2018.05.12

傳入socket前須將byte 轉成 byte 
才可進行socket 的 iostream 傳輸

(傳入/寫入socket)   encode():  string ==> byte   
(從socket接收/讀取) decode():  byte   ==> string 

"""

import socket
ip = socket.gethostbyname(socket.gethostname())	
#伺服端主機IP位址和連接埠號
HOST = ip
PORT = 5050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #連接伺服器
    s.connect((HOST, PORT))
except Exception as e:
    print('Server not found or not open')
    sys.exit()
    
c1 = input('Number1=')
#c2 = input('Number2=')

#傳送資料到伺服器端, 
#傳入socket前須先使用 encode()將 string 轉成 byte 以利 iostream 傳輸
#若不轉換成 byte 將造成錯誤
s.send(c1.encode())
#s.send(c2.encode())

#從伺服端接收資料, 並使用 decode() 將 byte 轉成 string
data = s.recv(1024).decode()
print('Receiving from Server:', data)

#關閉連接
s.close()
