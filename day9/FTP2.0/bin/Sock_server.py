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
        try:
           while True:
                print("got connection from", self.client_address)
                conn = self.request
                while True:
                    data = conn.recv(1024) #接收客户端发送的操作请求信息，根据请求类型做出对应操作
                    print('recv data:',data)
                    data = json.loads(data.decode())
                    print(data['user_path'])

                    if data.get('action') is not None:
                        if hasattr(self,'cmd_%s' %data['action']):
                            func = getattr(self,'cmd_%s' %data['action'])
                            func(data,conn)
        except ConnectionResetError as e:
            print('连接已断开',e)
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
        user_file = os.path.join(data['user_path'],data['filename']) #拼凑出需要存放的文件路径
        use_size = 0
        for parent, dirnames, filenames in os.walk(data['user_path']):
            for filename in filenames:
                use_size += os.path.getsize(os.path.join(parent, filename))
        print('use_size',use_size)
        if int(use_size)+int(data['size']) < int(data['space']):
            surplus_spcae=(int(data['space'])-int(use_size))/1024/1024
            surplus_spcae = round(surplus_spcae,2)
            #conn.send(('\033[1;31m剩余可用空间：%s M\033[0m' % surplus_spcae).encode())
            can_send = {'can_send':1}
            if os.path.isfile(user_file):
                can_send['if_continue'] = '1'
            else:
                can_send['if_continue'] = '0'
            conn.send(json.dumps(can_send).encode())
            conn.send(('\033[1;31m剩余可用空间：%s M\033[0m' % surplus_spcae).encode())
            if os.path.isfile(user_file):
                # if_continue = '1'
                # conn.send(if_continue.encode())
                is_file_szie =os.path.getsize(user_file)
                conn.send(str(is_file_szie).encode())
                file_obj = open(user_file, 'ab')
                while int(is_file_szie) < data['size']:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    is_file_szie += len(recv_data)
                    #print(data['size'], is_file_szie)
                else:
                    file_obj.flush()
                    file_obj.close()
                    print(data['size'], is_file_szie)
                    md5_02 = file_md5(user_file)
                    md5_get = md5_02.get_md5()
                    print(str(md5_get), data['file_md5'])
                    if str(md5_get) == data['file_md5']:
                        print('------successfully received file %s-----' % (data['filename']))
                        conn.send('\n\033[1;31m----send file done----\033[0m'.encode())
                    else:
                        print('\nmd5不一致,系统已自动删除该文件')
                        conn.send('\nmd5不一致,系统已自动删除该文件'.encode())
                        os.remove(user_file)
            else:
                # if_continue = '0'
                # conn.send(if_continue.encode())
                file_obj = open(user_file,'wb')
                received_size = 0

                while received_size < data['size']:#根据接收到的文件大小和服务端返回的文件大小判断文件是否传输完毕
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                    #print(data['size'],received_size)
                else:
                    file_obj.flush()
                    file_obj.close()
                    print(data['size'], received_size)
                    md5_02 = file_md5(user_file)
                    md5_get = md5_02.get_md5()
                    print(str(md5_get),data['file_md5'])
                    if str(md5_get) == data['file_md5']:
                        print('------successfully received file %s-----' % (data['filename']))
                        conn.send('\n\033[1;31m----send file done----\033[0m'.encode())
                    else:
                        print('md5不一致,系统已自动删除该文件')
                        conn.send('md5不一致,系统已自动删除该文件'.encode())
                        os.remove(user_file)
        else:
            print('\033[1;31m剩余空间不足，请联系管理员!\033[0m')
            can_send = {'can_send': 0}
            if os.path.isfile(user_file):
                can_send['if_continue'] = '1'
            else:
                can_send['if_continue'] = '0'
            conn.send(json.dumps(can_send).encode())
            conn.send('\033[1;31m剩余空间不足，请联系管理员!\033[0m'.encode())
            # if_continue = '0'
            # conn.send(if_continue.encode())


    def cmd_get(self,*args):
        data = args[0]
        conn = args[1]
        user_file = os.path.join(data['user_path'],data['filename']) #获取请求下载文件完整路径
        print(user_file)
        if os.path.isfile(user_file):
            file_size = os.path.getsize(user_file) #获得需要下载文件的大小
            md5_obj = file_md5(user_file)
            md5_get = md5_obj.get_md5()
            get_send = {
                'file_size':file_size,
                'md5_get':md5_get
            }
            conn.send(json.dumps(get_send).encode()) #发送给客户端
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
        print(data['user_path'])
        if os.path.isdir(data['user_path']):
            file_list = os.listdir(data['user_path'])
            conn.send(json.dumps(file_list).encode())
        else:
            print('xxxx')

    def cmd_cd(self,*args):
        data = args[0]
        conn = args[1]
        if os.path.isdir(os.path.join(data['user_path'],data['change_dir'])):
            conn.send('1'.encode())
            new_path = os.path.join(data['user_path'],data['change_dir'])
            conn.send(new_path.encode())
        else:
            conn.send('0'.encode())
            conn.send('\033[1;31m目录不存在！\033[0m'.encode())

    def cmd_cd_back(self,*args):
        data = args[0]
        conn = args[1]
        if os.path.basename(os.path.dirname(os.path.abspath(data['user_path']))) == 'user_data':
            conn.send('0'.encode())
            conn.send('\033[1;31m无法返回上级目录！\033[0m'.encode())
        else:
            conn.send('1'.encode())
            new_path = os.path.dirname(os.path.abspath(data['user_path']))
            conn.send(new_path.encode())

if __name__ == '__main__':
    Host,Port='localhost',8900
    server = socketserver.ThreadingTCPServer((Host,Port),Myserver)
    server.serve_forever()