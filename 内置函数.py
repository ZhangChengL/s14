#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
print(abs(-5))
print(all([0,-1,5]))
print(all([1,-1,3]))
print(any([0,-1,5]))
print(any([0]))

def ffunc(x,y):
    return x+y
print(list(map(ffunc,[1,2,3],[4,5,6])))

import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4]))
print(functools.reduce(lambda x,y:x+y,[1,2,3,4],10))

aa={1:4,-5:3,4:-1}
print(sorted(aa))
print(sorted(aa.items()))
print(sorted(aa.items(),key=lambda x:x[1]))