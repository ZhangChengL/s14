#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

num_a = 6
num_b = 0
while num_b < 3:
    num_c =int(input("input your num :"))
    if num_c > num_a:
        print("The num is too bigger")
    elif num_c < num_a:
        print("The num is too small")
    else:
        print("Bingo")
        break
    num_b = num_b +1
    if num_b == 3:
        countine = input("do you want to keep guessing?Y/N")
        if countine !="N":
            num_b =0
else:
     print("too many retrys! the right num is ",num_a)
