#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

info = {
    'stu001':'zzz',
    'stu002':'ccc',
    'stu003':'lll'
}
print(info)
print(info['stu001'])
info['stu001']='zcl' #修改，如果不存在就表示新增
print(info)
del info['stu003'] #删除  info.pop('stu003')  一样
print(info)
print(info.get('stu001')) #查找，推荐这种方法，不存在不会报错
info.setdefault('stu001','张') #添加，如果存在不改变
info.setdefault('stu005','xxxxxx')
print(info)

b = {
    1:2,
    2:3,
    'stu001':'zhang'
}
info.update(b)  #将字典b中的内容更新到字典info里面，存在的key就更新，不存在就新增
print(info)

for key in info:  #循环
    print(key,info[key])