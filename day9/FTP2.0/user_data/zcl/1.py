#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
rootdir = 'F:/Python/s14/day9/FTP2.0/file_data/zcl'
import os
import os.path

# this folder is custom
# rootdir = "D:/360Downloads/testFile1"
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        #print("parent folder is:" + parent)
        print(os.path.getsize(os.path.join(parent, filename)))


a = 9.918135643005371
print(type(int(round(a,2))))