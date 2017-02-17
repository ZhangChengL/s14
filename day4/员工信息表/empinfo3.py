#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import re
import os
staff_table="staff_table.txt"
staff_table_new="staff_table_new.txt"
staff_table_tmp="staff_table_tmp.txt"
path_exis =os.path.exists(staff_table)
if path_exis == False:
    exit('配置文件不存在，强制退出')
the_table_field={
        'staff_id':0,
        'name':1,
        'age':2,
        'phone':3,
        'dept':4,
        'enroll_date':5
    }
def path(): #判断临时文件是否存在
    path_exis_new=os.path.exists(staff_table_new)
    path_exis_tmp=os.path.exists(staff_table_tmp)
    if path_exis_new:
        os.remove(staff_table_new)
    if path_exis_tmp:
        os.remove(staff_table_tmp)

def file_open():#打开文件
    staff_old =open(staff_table,'r',encoding='utf-8')
    staff_new =open(staff_table_new,'w',encoding='utf-8')
    return  staff_old,staff_new

def file_tmp():#替换文件
    path_exis_tmp = os.path.exists(staff_table_tmp)
    if path_exis_tmp:
        os.remove(staff_table_tmp)
    os.rename(staff_table,staff_table_tmp)
    os.rename(staff_table_new,staff_table)

def add():#添加模块
    path()
    staff_old, staff_new = file_open()
    the_file_is_null = False#设置变量用来判断文件是否为空
    the_values = re.search('\(.*\)',str(sql_list)).group()#匹配出values后的内容
    the_values_into = the_values.split('(')[1].split(')')[0].split(',')#将values()括号内的值取出
    file_len = open(staff_table, 'r', encoding='utf-8')
    if len(file_len.read()) == 0:#判断表内是否有记录，如无记录则默认用户ID为1
        the_num_add = '1'
        the_file_is_null = True#文件为空，变量值变为True
    file_len.close()
    num_is=True
    if the_file_is_null ==False:#如果文件不为空，就依次匹配电话号码是否重复和获取ID
        for the_phone in staff_old:
            the_phone_list = the_phone.split()
            if the_phone_list[3] == the_values_into[2]:#依次匹配电话号码
                print('\033[1;31m电话号码重复！\033[0m')
                num_is=False#如果号码重复，则不进行下面的代码
                break
        if num_is==True:#如果电话号码不重复，num_is就不会变成false，就执行下面的写入记录代码
            to_find_num=open(staff_table,'r',encoding='utf-8')
            for num in to_find_num:
                num_list=num.split()
                the_num_add=str(int(num_list[0]) + 1)#轮训到表的最后一条记录取ID+1,就为新加入的记录的用户ID
                staff_new.write(num)
            the_values_into.insert(0,the_num_add)#将获取的ID插入等会需要写入文本的列表中
            print(the_values_into)
            the_values_into_list=' '.join(the_values_into)+'\n'
            staff_new.write(the_values_into_list)
            to_find_num.close()
            staff_old.close()
            staff_new.close()
            file_tmp()
            print('\033[1;31m添加成功\033[0m')
    else:#如果文件为空，就直接写入新文件
        the_values_into.insert(0, the_num_add)
        print(the_values_into)
        the_values_into_list = ' '.join(the_values_into) + '\n'
        staff_new.write(the_values_into_list)
        staff_old.close()
        staff_new.close()
        file_tmp()
        print('\033[1;31m添加成功\033[0m')

def remove():#删除模块
    path()
    staff_old, staff_new = file_open()
    for i in staff_old:
        if i.strip().startswith(sql_list[-1]):#匹配用户ID,如果相同就跳过写入以起到删除作用
            continue
        staff_new.write(i)
    staff_old.close()
    staff_new.close()
    file_tmp()
    print('\033[1;31m删除成功\033[0m')

def change():#修改模块
    path()
    staff_old, staff_new = file_open()
    change_num=0
    for i  in staff_old:
        a=re.split(' ',i)
        if  a[the_table_field[sql_list[-3]]]== sql_list[-1]:#匹配where后面的表名数据在文本中的位置然后再与需要的筛选的内容进行对比
            a[the_table_field[sql_list[3]]]=sql_list[5]#将需要修改的内容重新赋值进去
            a_into=' '.join(a)
            staff_new.write(a_into)
            change_num = change_num+1
            continue
        staff_new.write(i)
    staff_old.close()
    staff_new.close()
    file_tmp()
    print('\033[1;31m%s条记录已更新！\033[0m' %change_num)

def fetch():#查询模块
    path()
    staff_old, staff_new = file_open()
    if len(sql_list)== 4:#判断sql语句是否是条件查询语句
        if sql_list[1]=="*":#判断是否全部字段查询
            cont=0
            with open(staff_table,'r',encoding='utf-8') as f:
                for i in f :
                    print(i.replace('\n',''))
                    cont=cont+1
                print('\033[1;31m已查询到%s条内容\033[0m' %cont)
        if sql_list[1]!='*':#如果不是全部查询
            select_to_find=sql_list[1].split(',')
            for x in staff_old:
                find_output = []
                to_find = re.split(' ', x)
                for ff in select_to_find:
                    find_output.append(to_find[the_table_field[ff]])
                print(' '.join(find_output).replace('\n',''))

    def field_output():#判断是全部查询还是按表名查询
        if sql_list[1] != '*':
            select_to_find = sql_list[1].split(',')
            to_find_output = []
            for ff in select_to_find:
                to_find_output.append(to_find_where[the_table_field[ff]])
            print(' '.join(to_find_output))
        else:
            print(' '.join(to_find_where).replace('\n',''))

    if re.search("=|>|<|like",sql) is not None:#判断sql语句中是否有模糊查询
        change_num = 0
        num_is=False
        for i in staff_old:#以下匹配模糊查询类型
            to_find_where = re.split(' ', i)
            if sql_list[-2] == '=':
                if to_find_where[the_table_field[sql_list[-3]]] == sql_list[-1]:
                    field_output()
                    num_is = True
            if sql_list[-2] == '>':
                if int(to_find_where[the_table_field[sql_list[-3]]]) > int(sql_list[-1]):
                   field_output()
                   num_is = True
            if sql_list[-2] == '<':
                if int(to_find_where[the_table_field[sql_list[-3]]]) < int(sql_list[-1]):
                    field_output()
                    num_is = True
            if re.search('like',sql) is not None:
                if re.search(sql_list[-1],to_find_where[the_table_field[sql_list[-3]]]) is not None:
                    field_output()
                    num_is = True
            if num_is == True:#上面的代码只要匹配成功num_is=True就计数一次
                change_num = change_num + 1
                num_is = False
        print('\033[1;31m已查询到%s条内容\033[0m' % change_num)
    staff_old.close()
    staff_new.close()

while True:
    sql = input("请输入sql语句>>:")
    sql_list = re.split(' ', sql)
    if re.search("^(?i)insert into",sql) is not None and len(sql_list) ==4:
        add()
    elif  re.search("^(?i)delete", sql) is not None and len(sql_list) ==7:
        remove()
    elif re.search("^(?i)update", sql) is not None and len(sql_list) == 11:
        change()
    elif re.search("^(?i)select",sql) is not None:
        fetch()
    elif sql=='q' or sql == 'Q':
        exit()
    else:
        print("输入错误！")


