#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
print(len('D:\list_add'))
print(os.path.isfile('D:/Python/20170202/s14/day8/FTP/FTP作业要求.txt'))
print(os.path.isfile('D:\Python\20170202\s14\day8\FTP\FTP作业要求.txt'))
print(os.path.isfile('D:/list_add.txt'))