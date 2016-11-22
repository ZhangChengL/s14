#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#import  sys
#print(sys.argv)
import os
#cmd =os.system("dir") #执行命令，不保存结果
cmd =os.popen("dir").read()
print("----->",cmd)