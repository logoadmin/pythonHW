"""
TCP/IP Threaded Server sample

Author: Gwo-Chuan Lee 
Date: 2018.05.12

傳入socket前須將 string 轉成 byte 
才可進行socket 的 iostream 傳輸

(傳入/寫入socket)   encode():  string ==> byte   
(從socket接收/讀取) decode():  byte   ==> string 

"""

import socket
import threading

bind_ip = "192.168.0.122"
bind_port = 5050

#建立 TCP server socket 物件
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#繫結socket與 ip, port 
server.bind((bind_ip, bind_port))
#開始監聽用戶端連接            
server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
	#讀取客戶端的資料, 並使用 decode() 將 byte 轉成 string
	data1 = client_socket.recv(1024).decode() # Read Number 1
	data2 = client_socket.recv(1024).decode() # Read Number 2
	print("Number1=%s",data1)
	print("Number2=%s",data2)
	data=int(data1)+int(data2)
	print('Received: %s + %s = %d'%(data1,data2,data))
	
	#傳送資料到客戶端
	#傳入socket前須先使用 encode()將 string 轉成 byte 以利 iostream 傳輸
    #若不轉換成 byte 將造成錯誤
	client_socket.send(str(data).encode())
	client_socket.close()
	
while True: # 伺服器需不斷的測試是否有Client與之相連
    
	#取得與客戶端連結的位址 addr 與 Socket物件 client
	client, addr = server.accept()
	print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
	
	#呼叫 handle_client 產生一個與客戶端連線的 Thread
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start() # 啟動客戶端連線的 Thread 

#server.close()
	