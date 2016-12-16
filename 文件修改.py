#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
f = open('yesterday','r',encoding='utf-8')
f_new = open('yesterday.bak','w',encoding='utf-8')
for i in f:
    if '就如夜晚的微风' in i:
        i = i.replace('就如夜晚的微风','就如白天的微风') #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)
    f_new.write(i)
f.close()
f_new.close()