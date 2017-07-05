#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#from core import sockerclient
import socket
import os
import json
class User_manage(object):
    def __init__(self,account):
        self.account=account
    def server_client(self):
        Ps = '''\033[1;32m
        ============================================================
        Ps:
        上传文件格式：put x:/xxx/xxx（文件完整路径）
        下载文件格式：get xxx(文件名)  x:/xxx/xxx/ (需要存放的本地目录)
        查看目录下文件：ls
        ============================================================
        \033[0m'''
        print(Ps)

        client = socket.socket()
        Host, Port = 'localhost', 8900
        client.connect((Host, Port))

        while True:
            choice = input('>>>>>').strip()
            if len(choice) == 0:
                continue
            cmd_list = choice.split()

            if cmd_list[0] == 'put':
                if len(cmd_list) == 1:
                    print('请输入文件名！')
                    continue
                filename = cmd_list[1]
                if os.path.isfile(filename):
                    file_obj = open(filename, 'rb')
                    base_filename = os.path.basename(filename)
                    print(base_filename, os.path.getsize(filename))
                    data_header = {
                        'action': 'put',
                        'filename': base_filename,
                        'size': os.path.getsize(filename),
                        'account':self.account
                    }
                    client.send(json.dumps(data_header).encode())
                    for line in file_obj:
                        client.send(line)
                    print('----send file done----')

                else:
                    print('file is not valid')
                    continue

            elif cmd_list[0] == 'get':
                if len(cmd_list) == 3:
                    # print('请按正常格式输入！')
                    # continue
                    filename = cmd_list[1]
                    save_path = cmd_list[2]
                    save_file=os.path.join(save_path,filename)
                    if os.path.isdir(save_path):
                        if os.path.isfile(save_file) is not True:
                            data_header = {
                                'action':'get',
                                'filename':filename,
                                'save_file':save_file,
                                'account':self.account
                            }
                            client.send(json.dumps(data_header).encode())
                            return_size = client.recv(1024).decode()
                            print(return_size)
                            client.send('收到'.encode())
                            file_obj =open(save_file,'wb')
                            received_size = 0
                            while received_size < int(return_size):
                                recv_data = client.recv(4096)
                                file_obj.write(recv_data)
                                received_size += len(recv_data)
                                print(return_size,received_size)
                            else:
                                print('------successfully received file %s-----' % (save_file))
                                file_obj.close()
                        else:
                            print('目录下已存在相同文件名的文件！')
                    else:
                        print('目录不存在！')
                else:
                    print('输入错误！')

            elif cmd_list[0] == 'ls':
                data_header = {
                    'action':'ls',
                    'account':self.account
                }
                client.send(json.dumps(data_header).encode())
                return_list=client.recv(4096).decode()
                file_list = json.loads(return_list)
                for i in  file_list:
                    print(i)
            else:
                print('输入错误！')
