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
from core.file_md5 import file_md5
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
       while True:
           print("got connection from", self.client_address)
           conn = self.request
           while True:
                data = conn.recv(1024) #接收客户端发送的操作请求信息，根据请求类型做出对应操作
                print('recv data:',data)
                data = json.loads(data.decode())

                if data.get('action') is not None:
                    if hasattr(self,'cmd_%s' %data['action']):
                        func = getattr(self,'cmd_%s' %data['action'])
                        func(data,conn)
                    # if data['action'] == 'put':
                    #     user_path = setting.USER_FILE_PATH
                    #     user_file = os.path.join(user_path, data['account'],data['filename']) #拼凑出需要存放的文件路径
                    #     file_obj = open(user_file,'wb')
                    #     received_size = 0
                    #
                    #     while received_size < data['size']:#根据接收到的文件大小和服务端返回的文件大小判断文件是否传输完毕
                    #         recv_data = conn.recv(4096)
                    #         file_obj.write(recv_data)
                    #         received_size += len(recv_data)
                    #         print(data['size'],received_size)
                    #     else:
                    #         print('------successfully received file %s-----'%(data['filename']))
                    #         file_obj.close()
                    # elif data['action'] == 'get':
                    #     user_path = setting.USER_FILE_PATH #获取请求用户家目录
                    #     print(user_path)
                    #     user_file = os.path.join(user_path,data['account'],data['filename']) #获取请求下载文件完整路径
                    #     print(user_file)
                    #     if os.path.isfile(user_file):
                    #         file_size = os.path.getsize(user_file) #获得需要下载文件的大小
                    #         conn.send(str(file_size).encode()) #发送给客户端
                    #         client_final_ack = conn.recv(1024)
                    #         print('客户端应答：',client_final_ack.decode())#客户端接收到文件大小并进行应答
                    #         file_send = open(user_file,'rb')
                    #         for i in file_send: #发送需要下载文件的内容
                    #             conn.send(i)
                    #     else:
                    #         conn.send('文件不存在！'.encode())
                    # elif data['action'] == 'ls':
                    #     user_path = os.path.join(setting.USER_FILE_PATH,data['account'])
                    #     print(user_path)
                    #     if os.path.isdir(user_path):
                    #         file_list = os.listdir(user_path)
                    #         conn.send(json.dumps(file_list).encode())
    def cmd_put(self,*args):
        data = args[0]
        conn = args[1]
        user_path = setting.USER_FILE_PATH
        user_file = os.path.join(user_path, data['account'],data['filename']) #拼凑出需要存放的文件路径
        file_obj = open(user_file,'wb')
        received_size = 0

        while received_size < data['size']:#根据接收到的文件大小和服务端返回的文件大小判断文件是否传输完毕
            recv_data = conn.recv(4096)
            file_obj.write(recv_data)
            received_size += len(recv_data)
            print(data['size'],received_size)
        else:
            file_obj.close()
            md5_02 = file_md5(user_file)
            md5_get = md5_02.get_md5()
            print(str(md5_get))
            if str(md5_get) == data['file_md5']:
                print('------successfully received file %s-----' % (data['filename']))
            else:
                print('md5不一致')
    def cmd_get(self,*args):
        data = args[0]
        conn = args[1]
        user_path = setting.USER_FILE_PATH  # 获取请求用户家目录
        print(user_path)
        user_file = os.path.join(user_path,data['account'],data['filename']) #获取请求下载文件完整路径
        print(user_file)
        if os.path.isfile(user_file):
            file_size = os.path.getsize(user_file) #获得需要下载文件的大小
            conn.send(str(file_size).encode()) #发送给客户端
            client_final_ack = conn.recv(1024)
            print('客户端应答：',client_final_ack.decode())#客户端接收到文件大小并进行应答
            file_send = open(user_file,'rb')
            for i in file_send: #发送需要下载文件的内容
                conn.send(i)
        else:
            conn.send('文件不存在！'.encode())

    def cmd_ls(self,*args):
        data = args[0]
        conn = args[1]
        user_path = os.path.join(setting.USER_FILE_PATH,data['account'])
        print(user_path)
        if os.path.isdir(user_path):
            file_list = os.listdir(user_path)
            conn.send(json.dumps(file_list).encode())


if __name__ == '__main__':
    Host,Port='localhost',8900
    server = socketserver.ThreadingTCPServer((Host,Port),Myserver)
    server.serve_forever()