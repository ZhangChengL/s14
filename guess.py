#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

age = 22
for i in range(3):
    guess_age = int(input("请输入年龄："))
    if guess_age == age:
        print("yes! you are right")
        break
    elif guess_age > age:
        print("the age is too bigger")
    else:
        print("the age is too small")
else:
    print("你猜错太多次了！")