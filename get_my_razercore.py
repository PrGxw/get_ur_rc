#!/usr/bin/python
"""sources:
html parsing: http://www.boddie.org.uk/python/HTML.html
"""
import urllib.request
import util as util
import socket_util
import socket
import json

RETRIEVE_DATA = 0
SOCKET_CONNECTION = 1
NUM_TRIAL = 3

HOST = "149.28.44.30"  # '114.246.73.95'
PORT = 10101

if (SOCKET_CONNECTION):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 定义socket类型，网络通信，TCP
        s.bind((HOST, PORT))  # 套接字绑定的IP与端口
        s.listen(1)  # 开始TCP监听,监听1个请求
        
        print("Server is running")
        while True:
            conn, addr = s.accept(); # establish connection
            print("connected by", addr);

            with conn:
                msg = conn.recv(1024);  # received request code
                """ TODO: the naming of request code needs to be changed"""
                if msg.decode('utf-8') == "request": # if request code is: request
                    trial = 0;
                    response_code = ""
                    while trial < NUM_TRIAL:
                        try:
                            list = util.extract_info(); # aquire data
                        except Exception as e:
                            print(e)
                            trial += 1 # on fail, we go for another trial to retrieve data
                            print("tiral");
                            if trial == 3:
                                response_code = "ERROR\n";
                        else:
                            response_code = "DATA_\n"
                            break # if data retrieval we break out of he loop and send the data
                    conn.sendall(response_code.encode()); # send the response code
                    print("responseCode: " + response_code);
                    if response_code == "DATA_\n":
                        json_str = json.dumps(list); # convert to json string
                        conn.sendall(json_str.encode()); # send data
                    elif response_code == "ERROR\n":
                        conn.sendall("No Data Were Found!".encode());

                    
                else:
                    response_code = "NOREQ"
                    conn.sendall(response_code.encode())
                    conn.sendall(b"bye");
                





