#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff_table where age > 22
# 　　select  * from staff_table where dept = "IT"
#     select  * from staff_table where enroll_date like "2013"
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
a='select * from empinfo where age > 1'
# b='select name from empinfo where num = 1'
# c='select num,name from empinfo where enroll_date like "2013"'
print(re.split(' ',a))
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
def fetch(sql):
    if re.search("^(?i)select",sql) is None:
        print('输入错误')
    sql_list=re.split(' ',sql)
    if len(sql_list)== 4:
        if sql_list[3]!="empinfo"  :
            exit('输入的数据表不存在！')
        if sql_list[1]=="*":
            cont=0
            with open(staff_table,'r',encoding='utf-8') as f:
                for i in f :
                    print(i)
                    cont=cont+1
                print('已查询到%s条内容' %cont)
        if sql_list[1]!='*':
            select_to_find=[]
            select_to_find=sql_list[1].split(',')
            print(select_to_find)
def add(sql):
    path()
    staff_old, staff_new = file_open()
    if re.search("^(?i)insert into",sql) is None:
        print('输入错误')
    sql_list=re.split(' ',sql)
    print(sql_list)
   # aaa=re.search('(.*)',sql_list).group()
    cc = re.search('\(.*\)',str(sql_list)).group()
    ccc = cc.split('(')[1].split(')')[0].split(',')
    print(ccc)
    print(' '.join(ccc))
    file_len = open(staff_table, 'r', encoding='utf-8')
    if len(file_len.read()) == 0:
        aada_num = '1'
    file_len.close()
    num_is=True
    for aad in staff_old:
        ad_list = aad.split()
        if ad_list[3] == ccc[2]:
            print('电话号码重复！')
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

def remove(sql):
    pass
def change(sql):
    pass

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