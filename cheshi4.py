#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# for accmoney in acc_mon:
#     login_user, login_money = accmoney.strip().split()
#     loginuser = False
#     if yourname == login_user:
#
#         loginuser = True
#         print(loginuser)
#         print('尊敬的客户你好，你所剩余额为：\033[1;31m%s\033[0m' % login_money)
#         print(loginuser)
#         break
#     elif yourname != login_user:
#         break
#         # if loginuser == False:
#         #     yourmoney=input('第一次登录，请输入购物金额:')
#         #     user_money_add ='\n' + yourname +' '+ yourmoney
#         #     acc_mon.write(user_money_add)
#         #     print('金额录入成功，你所剩余额为：\033[1;31m%s\033[0m' %yourmoney)
#         # elif loginuser == True:
#         #     print('传递成功')
#     print(loginuser)
# def input_backend():
#     yourserver = input('input server:')
#     yourweight = input('input weight:')
#     yourmaxconn = input('input maxconn:')
#     your_new_server = 'server' + ' ' + yourserver + ' ' + 'weight' + ' ' + yourweight + ' ' + 'maxconn' + ' ' + yourmaxconn
#     return your_new_server,yourserver,yourweight,yourmaxconn
#
# x = input_backend(yourserver)
# print(x)
<<<<<<< HEAD

#
# dell='_'
# cc=['alex', 'eric', 'rain']
# aa=dell.join(cc)
# print(aa)
i = 2
a = 0
while i <101:
    if i % 2 == 0:
        a=a+i
    else:
        a=a-i
    i=i+1
print(a)
=======
import json
import os
# delimiter = ' '
# mylist = {    'server': '100.1.7.9',
#                'weight': 20,
 #               'maxconn': 30}
# print(delimiter.join(mylist))

#
# arg = input('arg:')
# yourserver = input('input server:')
# yourweight = input('input weight:')
# yourmaxconn = input('input maxconn:')
#
# #your_new_server = 'backend' + ' ' + arg + '\n' + '        ' + 'server' + ' ' + yourserver + ' ' + 'weight' + ' ' + yourweight + ' ' + 'maxconn' + ' ' + yourmaxconn + '\n'
# back = ['backend']
# ser = ['server','weight','maxconn']
# back.append(arg)
# ser.insert(ser.index('server')+1,yourserver)
# ser.insert(ser.index('weight')+1,yourweight)
# ser.insert(ser.index('maxconn')+1,yourmaxconn)
# dell = ' '
# print(dell.join(back))
# print(dell.join(ser))
# cc = open('111.txt','w')
# cc.write('1111')
# bb = open('222.txt','w')
# bb.write('2222')
# import os
# import shutil
# cc ="111.txt"
# bb ="222.txt"
# ff ="111_bak.txt"
# # ccc = open(cc,'r').read()
# # print(ccc)
# # shutil.copy(cc,'111_bak.txt')
# os.rename(bb,ff)
# def dad():
#     m=1
#     def son():
#         n=2
#         print ('--->',m + n)
#     print ('-->',m)
#     son()
# dad()
#
# def counter(start_num=0):
#     count = [start_num]
#
#     def incr():
#         count[0] += 1
#         return count[0]
#
#     return incr
#
#
# print(counter())
# print(counter()())
# print(counter()())
# c = counter()
# print(c())
# print(c())

#
# def decorartor(func):
#     def wrapper(n):
#         print('starting')
#         func(n)
#         print('stopping')
#
#     return wrapper
#
#
# def test(n):
#     print('in the test arg is %s' % n)
#
#
# decorartor(test)('alex')
# import math
# for i in range(10000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+268))
#     if  (x * x == i+100) and (y * y == i+268):
#         print(i)
#
# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)
#
# def fib(n):
# 	a,b = 1,1
# 	for i in range(n-1):
# 		a,b = b,a+b
# 	return a

# print(fib(10))
import os
# import time
# info={1:'a',2:'b',3:'c'}
# for key in info:
#     print(key,info[key])
#     time.sleep(1)
# i = 0
# while i<10:
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#     time.sleep(1)
#     i+=1
# from math import sqrt
# from sys import stdout
# leap = 0
# h = 0
# for m in range(101,201):
#     k = int(sqrt(m+1))
#     for i in range (2,k+1):
#         if m % i != 0:
#             print(m)
#             h +=1
# print('the total is %s'%h)
# for i in range (100,1000):
#     o = i // 100 # 取百位
#     p = i // 10 % 10 # 取十位
#     q = i % 10
#     if i == o ** 3  + p ** 3 + q ** 3:
#         print(i)
# i = 153
# o = i / 100 # 取百位
# p = i / 10 % 10 # 取十位
# q = i % 10
# # print(o,p,q)
# def calc(n):
#     print(n)
#     if int(n/2) ==0:
#         return n
#     return calc(int(n/2))
# # calc(10)
# def f(x):
#
#             return x*x
# print(list(map(f,[1,2,3,4,5])))
# name = "root"
# def func():
#     name = "seven"
#     def outer():
#         name = "eric"
#         def inner():
#             global name
#             name = "蒙逼了吧..."
#         print(name)
#     print(name)
#
# ret = func()
# print(ret)
# print(name)
# def f5(arg):
#     arg = arg + 5
#
# def f4(arg):
#     arg = arg + 4
#     f5(arg)
#     arg = arg + 4
#
# def f3(arg):
#     arg = arg + 3
#     f4(arg)
#     arg = arg + 3
#
# def f2(arg):
#     arg = arg + 2
#     f3(arg)
#     arg = arg + 2
#
# def f1(arg):
#     arg = arg + 1
#     f2(arg)
#     arg = arg + 1
#
# num = 1
# result = f1(num)
# print(num)
# print(result)
#
# def cc(x):
#     if x % 2 == 0:
#         return x+10
#     return x
# print(list(map(cc,[1,2,3,4,5])))
#
# def add(x,y,f):
#     return f(x)+f(y)
# res =add(3,-6,abs)
# print(res)
#
#
# def test01():
#     msg = 'hello The little green frog'
#     print(msg)
#
#
# def test02():
#     msg = 'hello WuDaLang'
#     print(msg)
#     return msg
#
#
# t1 = test01()
#
# t2 = test02()
#
# print('from test01 return is [%s]' % t1)
# print('from test02 return is [%s]' % t2)

#
# def test01():
#     pass
#
#
# def test02():
#     return 0
#
#
# def test03():
#     return 0, 10, 'hello', ['alex', 'lb'], {'WuDaLang': 'lb'}
#
#
# t1 = test01()
# t2 = test02()
# t3 = test03()
#
# print('from test01 return is [%s]: ' % type(t1), t1)
# print('from test02 return is [%s]: ' % type(t2), t2)
# print('from test03 return is [%s]: ' % type(t3), t3)

# def test1():
#     print('test1')
#     return test1
# print(test1())
import time
def timer(func): #timer(test1) func=test1
    def deco():
        start_time=time.time()
        func() #run test1()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return deco
@timer #test1=timer(test1)
def test1():
    time.sleep(3)
    print('this is test1')
test1()
>>>>>>> origin/master
