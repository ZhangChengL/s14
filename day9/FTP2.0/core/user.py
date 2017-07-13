#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#from core import sockerclient
import socket
import os
import json
import sys
from conf import setting
from core.file_md5 import file_md5
class User_manage(object):
    def __init__(self,account):
        self.account=account
    def server_client(self):
        print(setting.Ps)
        client = socket.socket()
        Host, Port = 'localhost', 8900

        try:
            client.connect((Host, Port))
            while True:
                choice = input('>>>>>').strip()
                if len(choice) == 0:
                    continue
                cmd_list = choice.split()

                # if cmd_list[0] == 'put': #发送文件到服务端
                #     if len(cmd_list) == 1:
                #         print('请输入文件名！')
                #         continue
                #     filename = cmd_list[1] #获取文件完整路径
                #     if os.path.isfile(filename):
                #         file_obj = open(filename, 'rb')
                #         base_filename = os.path.basename(filename) #获取文件名
                #         print(base_filename, os.path.getsize(filename))
                #         data_header = {
                #             'action': 'put',
                #             'filename': base_filename,
                #             'size': os.path.getsize(filename),
                #             'account':self.account
                #         }
                #         client.send(json.dumps(data_header).encode()) #发送准备发送的文件信息
                #         for line in file_obj:
                #             client.send(line)  #发送文件内容
                #         print('----send file done----')
                #
                #     else:
                #         print('file is not valid')
                #         continue
                #
                # elif cmd_list[0] == 'get': #从服务端获取文件
                #     if len(cmd_list) == 3:
                #         # print('请按正常格式输入！')
                #         # continue
                #         filename = cmd_list[1] #获取需要下载的文件名
                #         save_path = cmd_list[2] #获取需要存放的本地文件路径
                #         save_file=os.path.join(save_path,filename) #拼凑下载到本地的完整文件路径
                #         if os.path.isdir(save_path):
                #             if os.path.isfile(save_file) is not True:
                #                 data_header = {
                #                     'action':'get',
                #                     'filename':filename,
                #                     'save_file':save_file,
                #                     'account':self.account
                #                 }
                #                 client.send(json.dumps(data_header).encode())  #发送需要下载的文件信息
                #                 return_size = client.recv(1024).decode() #接收服务端发送的需要下载文件的大小
                #                 print(return_size)
                #                 client.send('收到'.encode())#接收到文件大小并进行应答
                #                 file_obj =open(save_file,'wb')
                #                 received_size = 0
                #                 while received_size < int(return_size): #根据接收到的文件大小和服务端返回的文件大小判断文件是否下载完毕
                #                     recv_data = client.recv(4096)
                #                     file_obj.write(recv_data)
                #                     received_size += len(recv_data)
                #                     print(return_size,received_size)
                #                 else:
                #                     print('------successfully received file %s-----' % (save_file))
                #                     file_obj.close()
                #             else:
                #                 print('目录下已存在相同文件名的文件！')
                #         else:
                #             print('目录不存在！')
                #     else:
                #         print('输入错误！')
                #
                # elif cmd_list[0] == 'ls':
                #     data_header = {
                #         'action':'ls',
                #         'account':self.account
                #     }
                #     client.send(json.dumps(data_header).encode()) #发送需要查看的用户名
                #     return_list=client.recv(4096).decode() #接收服务端发送的查询到的文件列表
                #     file_list = json.loads(return_list)
                #     for i in  file_list:
                #         print(i)
                # else:
                #     print('输入错误！')
                if hasattr(self,'cmd_%s'%cmd_list[0]):
                    func = getattr(self,'cmd_%s' %cmd_list[0])
                    func(cmd_list,client)
                else:
                    print('输入错误！')
        except ConnectionRefusedError as e:
            print('无法连接!',e)

    def cmd_put(self,*args):
        cmd_list = args[0]
        client = args[1]
        if len(cmd_list) > 1:
            filename = cmd_list[1]  # 获取文件完整路径
            if os.path.isfile(filename):
                file_obj = open(filename, 'rb')
                base_filename = os.path.basename(filename)  # 获取文件名
                print(base_filename, os.path.getsize(filename))
                md5_obj = file_md5(filename)
                md5_get = str(md5_obj.get_md5())
                data_header = {
                    'action': 'put',
                    'filename': base_filename,
                    'size': os.path.getsize(filename),
                    'account': self.account,
                    'file_md5':md5_get
                }
                client.send(json.dumps(data_header).encode())  # 发送准备发送的文件信息
                send_size = 0
                for line in file_obj:
                    client.send(line)  # 发送文件内容
                    send_size += len(line)
                    ret = send_size/(os.path.getsize(filename))
                    num = int(ret*100)
                    view = '\r%s%%%-100s'%(num,'\033[1;31m>\033[0m'*num)
                    sys.stdout.write(view)
                    sys.stdout.flush()
                # print('\n\033[1;31m----send file done----\033[0m')
                print(client.recv(1024).decode())

            else:
                print('file is not valid')
        else:
            print('输入错误！')

    def cmd_get(self,*args):
        cmd_list = args[0]
        client = args[1]
        if len(cmd_list) == 3:
            filename = cmd_list[1] #获取需要下载的文件名
            save_path = cmd_list[2] #获取需要存放的本地文件路径
            save_file=os.path.join(save_path,filename) #拼凑下载到本地的完整文件路径
            if os.path.isdir(save_path):
                if os.path.isfile(save_file) is not True:
                    data_header = {
                        'action':'get',
                        'filename':filename,
                        'save_file':save_file,
                        'account':self.account
                    }
                    client.send(json.dumps(data_header).encode())  #发送需要下载的文件信息
                    return_get = json.loads(client.recv(1024).decode()) #接收服务端发送的需要下载文件的大小

                    client.send('收到'.encode())#接收到文件大小并进行应答
                    file_obj =open(save_file,'wb')
                    received_size = 0
                    while received_size < int(return_get['file_size']): #根据接收到的文件大小和服务端返回的文件大小判断文件是否下载完毕
                        recv_data = client.recv(4096)
                        file_obj.write(recv_data)
                        received_size += len(recv_data)
                        print(return_get['file_size'],received_size)
                    else:
                        file_obj.close()
                        md5_obj = file_md5(save_file)
                        md5_get = str(md5_obj.get_md5())
                        if md5_get == return_get['md5_get']:
                            print('------successfully received file %s-----' % (save_file))
                        else:
                            print('md5值不一致，系统已自动删除该文件')
                            os.remove(save_file)

                else:
                    print('目录下已存在相同文件名的文件！')
            else:
                print('目录不存在！')
        else:
            print('输入错误！')

    def cmd_ls(self,*args):
        cmd_list = args[0]
        client = args[1]
        data_header = {
            'action':'ls',
            'account':self.account
        }
        client.send(json.dumps(data_header).encode()) #发送需要查看的用户名
        return_list=client.recv(4096).decode() #接收服务端发送的查询到的文件列表
        file_list = json.loads(return_list)
        for i in  file_list:
            print(i)

