#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl


s = set([3, 5, 9, 10,3])  # 创建一个数值集合
print(s)
t = set("Hello")  # 创建一个唯一字符的集合
print(t)
a = t | s  # t 和 s的并集
print(a)
b = t & s  # t 和 s的交集
print(b)
c = t - s  # 求差集（项在t中，但不在s中）
print(c)
d = t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）
print(d)
print(s.issubset(t))
s <= t    #测试是否s中的每一个元素都在t中

print(s.issuperset(t))
s >= t #测试是否t中的每一个元素都在s中

print(t in s) #测试x是否是s的成员

print(t not in s) #测试x是否不是s的成员