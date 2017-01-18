#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# 员工信息表程序，实现增删改查操作：
#
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff_table where age > 22
# 　　select  * from staff_table where dept = "IT"
#     select  * from staff_table where enroll_date like "2013"
# 查到的信息，打印后，最后面还要显示查到的条数
# 可创建新员工纪录，以phone做唯一键，staff_id需自增
# 可删除指定员工信息纪录，输入员工id，即可删除
# 可修改员工信息，语法如下:
# 　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
#  注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
import os
import time
staff_table="staff_table.txt"
staff_table_new="staff_table_new.txt"
staff_table_tmp="staff_table_tmp.txt"
# f=open(staff_table,'r',encoding='utf-8')
# c=0
# for i in f:
#     print(i)
#     c+=1
# print(c)
path_exis =os.path.exists(staff_table)
if path_exis == False:
    exit('配置文件不存在，强制退出')
def path(): #判断临时文件是否存在
    path_exis_new=os.path.exists(staff_table_new)
    path_exis_tmp=os.path.exists(staff_table_tmp)
    if path_exis_new:
        os.remove(staff_table_new)
    if path_exis_tmp:
        os.remove(staff_table_tmp)
def file_open():#文件操作
    staff_old =open(staff_table,'r',encoding='utf-8')
    staff_new =open(staff_table_new,'w',encoding='utf-8')
    return  staff_old,staff_new
def file_tmp():
    os.rename(staff_table,staff_table_tmp)
    os.rename(staff_table_new,staff_table)
    os.remove(staff_table_tmp)
def staff_input():
    name=input("请输入姓名：")
    if len(name)<2 or len(name)>6:
        exit("姓名输入错误！")
    age=input("请输入年龄：")
    if int(age)<=0 or age.isdigit()==False:
        exit("请输入正确的年龄")
    phone=input("请输入电话号码：")
    if len(phone)!=11 or phone.isdigit()==False:
        exit("请输入正确的手机号！")
    dept=input("清输入职位：")
    if dept.isalpha() == False:
        exit("请输入正确的职位：")
    enroll_date_year=input("请输入入职年份(例：2017)：")
    enroll_date_month = input("请输入入职年份(例：01)：")
    enroll_date_day= input("请输入入职年份(例：12)：")
    if enroll_date_year.isdigit()==False or enroll_date_month.isdigit()==False or enroll_date_day.isdigit()==False or len(enroll_date_year)!=4:
        exit("请输入正确的年月日")
    now_time_stamp=time.mktime(time.localtime()) #获取现在时间戳
    enroll_date_tmp = (enroll_date_year, enroll_date_month, enroll_date_day)
    enroll_date = '-'.join(enroll_date_tmp)
    enroll_date_stamp=time.mktime(time.strptime(enroll_date,'%Y-%m-%d'))
    if enroll_date_stamp > now_time_stamp:
        exit("请输入正确的日期")
    return name,age,phone,dept,enroll_date
#def ddel():#删除模块
path()
staff_old,staff_new=file_open()
num=input("请输入需要删除的员工id：")
for i in staff_old:
    if i.strip().startswith(num):
        continue
    staff_new.write(i)
staff_old.close()
staff_new.close()
file_tmp()
 #   pass
def add():#新增
    pass
def update():#更新
    pass
def select():#查询
    pass

meg='''
1.查询
2.新建
3.删除
4.修改
'''