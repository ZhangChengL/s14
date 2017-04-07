#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

class D:

    def bar(self):
        print ('D.bar')


class C(D):

    def bar(self):
        print ('C.bar')


class B(D):

    def bar(self):
        print ('B.bar')


class A(B, C):

    def bar(self):
        print ('A.bar')

a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()


class D(object):

    def bar(self):
        print ('D.bar')


class C(D):

    def bar(self):
        print ('C.bar')


class B(D):

    def bar(self):
        print ('B.bar')


class A(B, C):

    def bar(self):
        print ('A.bar')

a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()


class Province:

    # 静态字段
    country = '中国'

    def __init__(self, name):

        # 普通字段
        self.name = name
        print(Province.country)


# 直接访问普通字段
obj = Province('河北省')
print (obj.name)

# 直接访问静态字段
print(Province.country)
#################
class C:

    name = "公有静态字段"

    def func(self):
        print(C.name)

class D(C):

    def show(self):
        print(C.name)


print(C.name)         # 类访问

obj = C()
obj.func()     # 类内部可以访问

obj_son = D()
obj_son.show() # 派生类中可以访问
