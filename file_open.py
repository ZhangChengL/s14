#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#data = open('yesterday',encoding='utf-8').read()
#print(data)
'''
file = open('yesterday','a',encoding='utf-8')
#f=file.read()
file.write('\n11111111111111111111111111111\n'.center(50,'-'))
f = file.read()
print(f)
file_line = file.readline()
for i in file:
    print(i)

file.close()'''
'''
f = open('yesterday','r+',encoding='utf-8')
f.write('---------------------------------')
print(f.read())
'''
import sys,time
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.2)