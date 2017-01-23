#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import time
staff_table="staff_table.txt"
staff_table_new="staff_table_new.txt"
staff_table_tmp="staff_table_tmp.txt"
phone_count=3
meg='''
\033[1;32m
***********************************
1.查询
2.新建
3.删除
4.修改
5.退出
***********************************
\033[0m
'''
meg_cx='''
\033[1;32m
***********************************
1.按员工ID查询
2.按姓名查询
3.按年龄查询
4.按电话号码查询
5.按职位查询
6.按入职年份查询
7.退出查询
************************************
\033[0m
'''

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
    path_exis_tmp = os.path.exists(staff_table_tmp)
    if path_exis_tmp:
        os.remove(staff_table_tmp)
    os.rename(staff_table,staff_table_tmp)
    os.rename(staff_table_new,staff_table)
    # os.remove(staff_table_tmp)
    # os.remove(staff_table_new)
def staff_input():
    while True:
        name = input("请输入姓名：")
        if len(name) < 2 :
            print("姓名输入错误！请重新输入")
            continue
        age = input("请输入年龄：")
        if  age.isdigit() == False:
            print("年龄输入错误！请重新输入")
            continue
        if int(age)<=0:
            print("年龄输入错误！请重新输入")
            continue
        phone = input("请输入电话号码：")
        if len(phone) != 11 or phone.isdigit() == False:
            print("号码输入错误！请重新输入")
            continue
        dept = input("请输入职位：")
        if dept.isalpha() == False:
            print("职位输入错误！请重新输入")
            continue
        enroll_date_year = input("请输入入职年份(例：2017)：")
        enroll_date_month = input("请输入入职年份(例：01)：")
        enroll_date_day = input("请输入入职年份(例：12)：")
        if enroll_date_year.isdigit() == False or enroll_date_month.isdigit() == False or enroll_date_day.isdigit() == False or len(
                enroll_date_year) != 4:
            print("请输入正确的年月日！")
            continue
        now_time_stamp = time.mktime(time.localtime())  # 获取现在时间戳
        enroll_date_tmp = (enroll_date_year, enroll_date_month, enroll_date_day)
        enroll_date = '-'.join(enroll_date_tmp)
        enroll_date_stamp = time.mktime(time.strptime(enroll_date, '%Y-%m-%d'))
        if enroll_date_stamp > now_time_stamp:
            print("请输入正确的日期！")
            continue
        return name, age, phone, dept, enroll_date

while True:
    print(meg)
    choice=input('请选择：')
    if choice.isdigit():
        choices=int(choice)
        if choices==1:
            while True:
                print(meg_cx)
                cx_choice=input('请选择：')
                if cx_choice.isdigit():
                    cx_choices=int(cx_choice)
                    if cx_choices==6:
                        find_of_time = 0
                        your_find = input('请输入需要查询年份(例：2016)：')
                        with open(staff_table,'r',encoding='utf-8') as ff:
                            for ii in ff:
                                a=ii.split(' ')
                                b=a[cx_choices-1].split('-')
                                b_year=b[0]
                                if b_year == your_find:
                                    print(' '.join(a))
                                    find_of_time+=1
                        print('\033[1;31m已查询到%s条数据\033[0m' % find_of_time)
                    if cx_choices==7:
                        break
                    if cx_choices in (1,2,4,5):
                        find_of_other=0
                        your_find=input('请输入需要查询的内容：')
                        with open(staff_table, 'r', encoding='utf-8') as f:
                            for i in f:
                                a = i.split(' ')
                                if a[cx_choices-1] == your_find:
                                    cc=' '.join(a)
                                    print(cc)
                                    find_of_other+=1
                        print('\033[1;31m已查询到%s条数据\033[0m' % find_of_other)
                    if cx_choices==3:
                        find_of_age=0
                        your_find_age = input('请输入需要查询的年龄范围，用空格分割（例：25 30）：')
                        your_find_ages=your_find_age.split()
                        if len(your_find_ages)==2:
                            if your_find_ages[0].isdigit() and your_find_ages[1].isdigit():
                                if int(your_find_ages[0])>int(your_find_ages[1]):
                                    your_find_ages[0],your_find_ages[1]=your_find_ages[1],your_find_ages[0]
                        elif len(your_find_ages)==1:
                            your_find_ages.append(100)
                        else:
                            print('输入错误！')
                            break
                        if your_find_ages[0].isdigit() and your_find_ages[1].isdigit():
                            with open(staff_table, 'r', encoding='utf-8') as f:
                                for i in f:
                                    a = i.split(' ')
                                    if int(a[cx_choices-1]) >= int(your_find_ages[0]) and int(a[cx_choices-1]) <= int(your_find_ages[1]):
                                        cc=' '.join(a)
                                        print(cc)
                                        find_of_age+=1
                            print('\033[1;31m已查询到%s条数据\033[0m' % find_of_age)
                        else:
                            print('输入错误！')
                            break
                else:
                    print('\033[1;31m输入错误！\033[0m')
        if choices==2:
            path()
            staff_old,staff_new=file_open()
            add_name, add_age, add_phone, add_dept, add_enroll_date = staff_input()
            file_len=open(staff_table,'r',encoding='utf-8')
            if len(file_len.read())==0:
                ad_num=1
            file_len.close()
            for aad in staff_old:
                staff_new.write(aad)
                ad_list = aad.split()
                ad_num = int(ad_list[0]) + 1
                phone_input=1
                if ad_list[3] ==add_phone:
                    while True:
                        print('\033[1;31m电话号码重复，请确认号码重新输入！\033[0m')
                        add_phone = input("请输入电话号码：")
                        if len(add_phone) != 11 or add_phone.isdigit() == False:
                            print("\033[1;31m请输入正确的手机号！\033[0m")
                        if ad_list[3] !=add_phone:
                            break
                        phone_input+=1
                        if phone_input == phone_count:
                            exit('电话输入重复多次，强制退出！')
            add_list = [str(ad_num), add_name, add_age, add_phone, add_dept,add_enroll_date]
            print(add_list)
            add_staff_into = ' '.join(add_list)+'\n'
            staff_new.write(add_staff_into)
            staff_old.close()
            staff_new.close()
            file_tmp()
        if choices==3:
            staff_old, staff_new = file_open()
            num = input("请输入需要删除的员工id：")
            if num.isdigit():
                for i in staff_old:
                    if i.strip().startswith(num):
                        continue
                    staff_new.write(i)
            else:
                print('\033[1;31m输入错误！\033[0m')
                break
            print('\033[1;31m删除成功！\033[0m')
            staff_old.close()
            staff_new.close()
            file_tmp()
        if choices==4:
            path()
            staff_old,staff_new=file_open()
            you_want_up=input('请输入需要被修改的内容：')
            you_new_up=input('请输入修改后的内容：')
            for xx in staff_old:
                find_up=xx.split()
                if you_want_up in find_up:
                    find_num=find_up.index(you_want_up)
                    find_up.remove(you_want_up)
                    find_up.insert(find_num,you_new_up)
                    up_staff_into = ' '.join(find_up) + '\n'
                    staff_new.write(up_staff_into)
                else:
                    staff_new.write(xx)
            print('\033[1;31m更新成功！\033[0m')
            staff_old.close()
            staff_new.close()
            file_tmp()
        if choices==5:
            exit()
    else:
        print('输入错误，请重新输入')