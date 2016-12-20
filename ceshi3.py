#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
acc_mon = open('byacc','r+')
a = input('name')
for acc_mons in acc_mon:
    (acc_use, acc_money) = acc_mons.strip().split()
    print(acc_use)
     a not  acc_use:
        print(acc_money)