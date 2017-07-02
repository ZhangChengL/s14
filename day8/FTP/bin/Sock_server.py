#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import socket
import json
import socketserver
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
                        file_obj = open(data['filename'],'wb')
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
                    pass

if __name__ == '__main__':
    Host,Port='localhost',8900
    server = socketserver.ThreadingTCPServer((Host,Port),Myserver)
    server.serve_forever()