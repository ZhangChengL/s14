#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
'''
name = ['zcl','zzz','ccc','lll']
print(name[1])
name.append('zhang')
name.append('zhang')
print(name)
print(name.count('zhang'))
print(name.index('zzz'))
name.insert(3,'cl')
print(name)
name.pop()
print(name)
name.remove('zhang')
print(name)'''
'''
name = ['zcl','zzz','ccc','lll','zhang','zhang']
print(name)
for i in range(name.count('zhang')):
    name.remove('zhang')
print(name)
'''
a = [1,2,3]
b = a
print(a)
print(b)
a[1] = 555
print(a)
print(b)