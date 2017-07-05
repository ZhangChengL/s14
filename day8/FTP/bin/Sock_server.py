#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import socket
import json
import socketserver
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from conf import setting
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
       while True:
           print("got connection from", self.client_address)
           conn = self.request
           while True:
                data = conn.recv(1024)
                print('recv data:',data)
                data = json.loads(data.decode())

                if data.get('action') is not None:
                    if data['action'] == 'put':
                        user_path = setting.USER_FILE_PATH
                        user_file = os.path.join(user_path, data['account'],data['filename'])
                        file_obj = open(user_file,'wb')
                        received_size = 0

                        while received_size < data['size']:
                            recv_data = conn.recv(4096)
                            file_obj.write(recv_data)
                            received_size += len(recv_data)
                            print(data['size'],received_size)
                        else:
                            print('------successfully received file %s-----'%(data['filename']))
                            file_obj.close()
                    elif data['action'] == 'get':
                        user_path = setting.USER_FILE_PATH
                        print(user_path)
                        user_file = os.path.join(user_path,data['account'],data['filename'])
                        print(user_file)
                        if os.path.isfile(user_file):
                            file_size = os.path.getsize(user_file)
                            conn.send(str(file_size).encode())
                            client_final_ack = conn.recv(1024)
                            print('客户端应答：',client_final_ack.decode())
                            file_send = open(user_file,'rb')
                            for i in file_send:
                                conn.send(i)
                        else:
                            conn.send('文件不存在！'.encode())
                    elif data['action'] == 'ls':
                        user_path = os.path.join(setting.USER_FILE_PATH,data['account'])
                        print(user_path)
                        if os.path.isdir(user_path):
                            file_list = os.listdir(user_path)
                            conn.send(json.dumps(file_list).encode())


if __name__ == '__main__':
    Host,Port='localhost',8900
    server = socketserver.ThreadingTCPServer((Host,Port),Myserver)
    server.serve_forever()