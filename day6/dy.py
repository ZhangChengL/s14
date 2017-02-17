#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import re
aaa='小于5G的片单.txt'
bbb='电影0214.txt'
aaa_open=open(aaa,'r',encoding='utf-8')
bbb_open=open(bbb,'r',encoding='utf-8')
cc=0
for i in aaa_open:
    for f in bbb_open:
        if f==i:
            print(f)
            cc=cc+1
print(cc)