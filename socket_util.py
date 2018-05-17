import socket

HOST= "127.0.0.1" #'114.246.73.95'
PORT= 10101

def server_run():
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
    s.bind((HOST,PORT))   #套接字绑定的IP与端口
    s.listen(1)         #开始TCP监听,监听1个请求
    print("Server is running")
    while 1:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            # while True:
            #     data = conn.recv(1024)
            #     if not data: break
            #     conn.sendall(data)

    conn.close()     #关闭连接