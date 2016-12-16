#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
g = open('good','r',encoding='utf-8')
good =g.read()
print(type(good))
good_s= eval(good)
print(type(good_s))
print(good_s)