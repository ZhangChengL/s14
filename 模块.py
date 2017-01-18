#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# import time
# import datetime
#
# print(time.asctime())
# t=time.localtime()
# print(t)
# print(t.tm_year,t.tm_mon,t.tm_yday)
# ccc='2016/07/18'
# string_2_struct = time.strptime(ccc,"%Y/%m/%d") #字符串转为时间对象
# print(string_2_struct)
# struct_2_stamp = time.mktime(string_2_struct) #时间对象转为时间戳
# print(struct_2_stamp)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # 时间搓转为字符串
# print(time.localtime()) #时间对象
# print(time.time()) #时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #时间对象转为字符串


# import random
# import string
# print(random.random()) #随机一个小数
# print(random.randint(1,5)) #随机一个1-5
# print(random.randrange(1,10)) #随机一个1-9，不包含10
# print(random.sample(range(100),5))  #在1-100里面随机选5个数
# str_source = string.ascii_letters + string.digits
# print(''.join(random.sample(str_source,4)))  #生成一个4位随机数
#
# checkcode = ''
# for i in range(4):
#     current = random.randrange(0,4)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
# print(checkcode)
# import time
# print(time.strftime('%Y',time.localtime()))
#
# ccc='2016/7/18'
# bbb='2017/04/12'
# string_2_struct = time.strptime(ccc,"%Y/%m/%d")
# struct_2_stamp = time.mktime(string_2_struct)
# string_3_struct =time.localtime()
# struct_3_stamp = time.mktime(string_3_struct)
# if string_2_struct < string_3_struct:
#     print('ok')
# else:
#     print('NO')
#
# enroll_date_year=input("请输入入职年份(例：2017)：")
# enroll_date_month = input("请输入入职年份(例：01)：")
# enroll_date_day= input("请输入入职年份(例：12)：")
# enroll_date_tmp=(enroll_date_year,enroll_date_month,enroll_date_day)
# enroll_date='-'.join(enroll_date_tmp)
# print(enroll_date)
# import  time
# def xxx():
#     for i in range(3):
#         name = input("请输入姓名：")
#         if len(name) < 2 or len(name) > 6:
#             print("姓名输入错误！")
#             c
#         age = input("请输入年龄：")
#         if int(age) <= 0 or age.isdigit() == False:
#             print("请输入正确的年龄")
#             break
#         phone = input("请输入电话号码：")
#         if len(phone) != 11 or phone.isdigit() == False:
#             print("请输入正确的手机号！")
#             break
#         dept = input("清输入职位：")
#         if dept.isalpha() == False:
#             print("请输入正确的职位：")
#             break
#         enroll_date_year = input("请输入入职年份(例：2017)：")
#         enroll_date_month = input("请输入入职年份(例：01)：")
#         enroll_date_day = input("请输入入职年份(例：12)：")
#         now_time_stamp = time.mktime(time.localtime())  # 获取现在时间戳
#         enroll_date_tmp = (enroll_date_year, enroll_date_month, enroll_date_day)
#         enroll_date = '-'.join(enroll_date_tmp)
#         enroll_date_stamp = time.mktime(time.strptime(enroll_date, '%Y-%m-%d'))
#         if enroll_date_stamp > now_time_stamp:
#             print("请输入正确的日期")
#             break


