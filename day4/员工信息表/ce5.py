#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
f=open('staff_table.txt','r',encoding='utf-8')
for i in f:
    a=i.split(' ')
    if a[-2]=='IT':
        print(a)
