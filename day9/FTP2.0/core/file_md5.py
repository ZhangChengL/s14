#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import hashlib
class file_md5(object):
    def __init__(self,file_name):
        self.file_name = file_name
    def get_md5(self):
        f = open(self.file_name, 'rb')
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5

if __name__ == "__main__":
  file_path = 'F:/my_send.txt'
  md5_02 = file_md5(file_path)
  md5_get = str(md5_02.get_md5())
  print(md5_get)
  print(type(md5_get))