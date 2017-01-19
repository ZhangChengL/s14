#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
f=open('staff_table.txt','r',encoding='utf-8')
staff_table="staff_table.txt"
staff_old =open(staff_table,'r',encoding='utf-8')
# for i in f:
#     a=i.split(' ')
#     if a[-2]=='IT':
#         print(a)
# for i in f:
#     print(i)
#     if i.strip()=='':
#         print('yes')
#     else:
#         print('No')
for i in staff_old:
    print(i)