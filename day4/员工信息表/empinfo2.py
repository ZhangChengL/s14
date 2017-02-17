#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff_table where age > 22
# 　　select  * from staff_table where dept = IT
#     select  * from staff_table where enroll_date like 2013
# 查到的信息，打印后，最后面还要显示查到的条数
# 可创建新员工纪录，以phone做唯一键，staff_id需自增
#insert into emp values(xxx,xx,xx,xx,xx)
# 可删除指定员工信息纪录，输入员工id，即可删除
# delete from emp where num = 1;
# 可修改员工信息，语法如下:
# 　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
#  注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
import re
import os
staff_table="staff_table.txt"
staff_table_new="staff_table_new.txt"
staff_table_tmp="staff_table_tmp.txt"
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
chag={
        'staff_id':0,
        'name':1,
        'age':2,
        'phone':3,
        'dept':4,
        'enroll_date':5
    }
def fetch(sql):
    path()
    staff_old, staff_new = file_open()
    # if re.search("^(?i)select",sql) is None:
    #     print('\033[1;31m输入错误\033[0m')
    sql_list=re.split(' ',sql)
    if len(sql_list)== 4:
        if sql_list[1]=="*":
            cont=0
            with open(staff_table,'r',encoding='utf-8') as f:
                for i in f :
                    print(i)
                    cont=cont+1
                print('\033[1;31m已查询到%s条内容\033[0m' %cont)
        if sql_list[1]!='*':
            select_to_find=[]
            select_to_find=sql_list[1].split(',')
            # print(select_to_find)
            for x in staff_old:
                cc_output = []
                aa = re.split(' ', x)
                for ff in select_to_find:
                    cc_output.append(aa[chag[ff]])
                print(' '.join(cc_output))

    if re.search("=|>|<|like",sql) is not None:
        change_num = 0
        num_is=False
        for i in staff_old:
            aa = re.split(' ', i)
            if sql_list[-2] == '=':
                if aa[chag[sql_list[-3]]] == sql_list[-1]:
                    if sql_list[1]!='*':
                        select_to_find = sql_list[1].split(',')
                        cc_output = []
                        for ff in select_to_find:
                            cc_output.append(aa[chag[ff]])
                        print(' '.join(cc_output))
                        num_is = True
                    else:
                        print(' '.join(aa))
                        num_is=True
            if sql_list[-2] == '>':
                if int(aa[chag[sql_list[-3]]]) > int(sql_list[-1]):
                    if sql_list[1]!='*':
                        select_to_find = sql_list[1].split(',')
                        cc_output = []
                        for ff in select_to_find:
                            cc_output.append(aa[chag[ff]])
                        print(' '.join(cc_output))
                        num_is = True
                    else:
                        print(' '.join(aa))
                        num_is=True
            if sql_list[-2] == '<':
                if int(aa[chag[sql_list[-3]]]) < int(sql_list[-1]):
                    if sql_list[1]!='*':
                        select_to_find = sql_list[1].split(',')
                        cc_output = []
                        for ff in select_to_find:
                            cc_output.append(aa[chag[ff]])
                        print(' '.join(cc_output))
                        num_is = True
                    else:
                        print(' '.join(aa))
                        num_is=True
            if re.search('like',sql) is not None:
                if re.search(sql_list[-1],aa[chag[sql_list[-3]]]) is not None:
                    if sql_list[1]!='*':
                        select_to_find = sql_list[1].split(',')
                        cc_output = []
                        for ff in select_to_find:
                            cc_output.append(aa[chag[ff]])
                        print(' '.join(cc_output))
                        num_is = True
                    else:
                        print(' '.join(aa))
                        num_is=True
            if num_is == True:
                change_num = change_num + 1
                num_is = False
        print('\033[1;31m已查询到%s条内容\033[0m' % change_num)
    staff_old.close()
    staff_new.close()
def field_output():
    if sql_list[1] != '*':
        select_to_find = sql_list[1].split(',')
        cc_output = []
        for ff in select_to_find:
            cc_output.append(aa[chag[ff]])
        print(' '.join(cc_output))
        num_is = True
    else:
        print(' '.join(aa))
        num_is = True


def add(sql):
    path()
    staff_old, staff_new = file_open()
    # sql_list = re.split(' ', sql)
    # if re.search("^(?i)insert into",sql) is None or len(sql_list) !=4:
    #     exit('输入错误')
    cc = re.search('\(.*\)',str(sql_list)).group()
    ccc = cc.split('(')[1].split(')')[0].split(',')
    file_len = open(staff_table, 'r', encoding='utf-8')
    if len(file_len.read()) == 0:
        aada_num = '1'
    file_len.close()
    num_is=True
    for aad in staff_old:
        ad_list = aad.split()
        if ad_list[3] == ccc[2]:
            print('\033[1;31m电话号码重复！\033[0m')
            num_is=False
            break
    if num_is==True:
        fff=open(staff_table,'r',encoding='utf-8')
        for aada in fff:
            aada_list=aada.split()
            aada_num=str(int(aada_list[0]) + 1)
            staff_new.write(aada)
        ccc.insert(0,aada_num)
        print(ccc)
        ccc_num=' '.join(ccc)+'\n'
        staff_new.write(ccc_num)
        fff.close()
        staff_old.close()
        staff_new.close()
        file_tmp()
    print('\033[1;31m添加成功\033[0m')
def remove(sql):
    path()
    staff_old, staff_new = file_open()
    sql_list = re.split(' ', sql)
    if re.search("^(?i)delete", sql) is None or len(sql_list)!=7:
        exit('输入错误')
    for i in staff_old:
        if i.strip().startswith(sql_list[-1]):
            continue
        staff_new.write(i)
    staff_old.close()
    staff_new.close()
    file_tmp()
    print('\033[1;31m删除成功\033[0m')
def change(sql):
    path()
    staff_old, staff_new = file_open()
    sql_list = re.split(' ', sql)
    if re.search("^(?i)update", sql) is None or len(sql_list) != 10 :
        exit('输入错误')
    change_num=0
    for i  in staff_old:
        aa=re.split(' ',i)
        if  aa[chag[sql_list[-3]]]== sql_list[-1]:
            aa[chag[sql_list[3]]]=sql_list[5]
            aa_into=' '.join(aa)
            staff_new.write(aa_into)
            change_num = change_num+1
            continue
        staff_new.write(i)
    staff_old.close()
    staff_new.close()
    file_tmp()
    print('\033[1;31m%s条记录已更新！\033[0m' %change_num)
msg = """
    1:查询
    2:添加
    3:删除
    4:修改
    5:退出
    """
msg_dict = {
    "1": fetch,
    "2": add,
    "3": remove,
    "4": change,
    "5": exit,
    }
while True:
    print(msg)
    choice = input("输入序号>>:")
    if len(choice) == 0 or choice not in msg_dict:
        print('输入错误')
        continue
    if choice =='5':
        exit()
    sql = input("请输入sql语句>>:")
    msg_dict[choice](sql)