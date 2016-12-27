#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import json
import os
import shutil
def haproxy_find(arg):
    bg = False
    cx = []
    with open('haproxy.txt','r',encoding='utf-8') as f:
        for i in f:
            if i.strip() == "backend %s" %arg:
                #print(i)
                bg=True
                continue
            if i.strip().startswith('backend'):
                bg = False
            if bg == True:
                cx.append(i)
    return cx
def haproxy_add(arg):
    ha = False
    hadd = open('haproxy.txt','r+',encoding='utf-8')
    for x in hadd:
        if x.strip() == 'backend %s' %arg:
            ha = True
    if ha == True:
        add_choise=input('\033[1;31mbackend信息已存在，继续操作将更新backend信息！请选择是否继续y/n:\033[0m')
        if add_choise == 'y':
            hadd.close()
            hap_add_upp=haproxy_update(arg)
        else:
            exit('已退出！')
    if ha == False:
        #print('没匹配到，新增')
        yourserver = input('input server:')
        yourweight = input('input weight:')
        yourmaxconn = input('input maxconn:')
        your_new_server ='backend'+' '+ arg +'\n'+'        '+'server'+' '+yourserver+' '+'weight'+' '+yourweight+' '+'maxconn'+' '+yourmaxconn+'\n'
        hadd.write(your_new_server)
        hadd.close()
#这是新增板块的
#如果存在就删除，不存在就退出
def haproxy_delete(arg):
    hup_del = open('haproxy.txt','r',encoding='utf-8')
    hup_del_exis = open('haproxy.txt','r',encoding='utf-8')
    hup_del_new = open('haproxy_new','w',encoding='utf-8')
    hup_del_is = False
    hup_exis_is =False
    for hd_exis in hup_del_exis:
        if hd_exis.strip() ==  'backend %s' %arg:
            hup_exis_is = True
            break
    if hup_exis_is == False:
        exit('你输入的backend信息不存在！')
    for hd in hup_del:
        if hd.strip() == 'backend %s' %arg:
            hup_del_is = True
            continue
        if hd.strip().startswith('backend'):
            hup_del_is = False
        if hup_del_is == False:
            hup_del_new.write(hd)
    hup_del_new.close()
    hup_del.close()
    hup_del_exis.close()
    os.remove('haproxy_bak.txt')
    shutil.copy('haproxy.txt', 'haproxy_bak.txt')
    os.rename('haproxy.txt', 'haproxy_tmp')
    os.rename('haproxy_new', 'haproxy.txt')
    os.remove('haproxy_tmp')

def haproxy_update(arg):
    hup = open('haproxy.txt','r',encoding='utf-8')
    hup_new = open('haproxy_new','w',encoding='utf-8')
    hup_add_exis = open('haproxy.txt','r',encoding='utf-8')
    hup_add_is = False
    hup_is = False
    for huadd_exis in hup_add_exis:
        if huadd_exis.strip() == 'backend %s' %arg:
            hup_add_is = True
            break
    if hup_add_is == False:
        exit('你输入的backend信息不存在！')
    for c in hup:
        if c.strip() == 'backend %s' %arg:
            hup_is = True
            continue
        if c.strip().startswith('backend'):
            hup_is = False
        if hup_is == True:
            yourserver = input('input server:')
            yourweight = input('input weight:')
            yourmaxconn = input('input maxconn:')
            your_new_server ='backend'+' '+ arg +'\n' + '        ' + 'server' + ' ' + yourserver + ' ' + 'weight' + ' ' + yourweight + ' ' + 'maxconn' + ' ' + yourmaxconn+'\n'
            hup_new.write(your_new_server)
            continue
        hup_new.write(c)
    hup_new.close()
    hup.close()
    hup_add_exis.close()
    os.remove('haproxy_bak.txt')
    shutil.copy('haproxy.txt','haproxy_bak.txt')
    os.rename('haproxy.txt','haproxy_tmp')
    os.rename('haproxy_new','haproxy.txt')
    os.remove('haproxy_tmp')
    #如果存在就更新，不存在就退出
meg = '''
\033[1;32m=======================Welcome====================
1.查找backend信息
2.添加backend信息
3.更新backend信息
4.删除backend信息
5.退出\033[0m
'''

while True:
    print(meg)
    your_choise = input('\033[1;31m请选择：\033[0m')
    if your_choise == '1':
         backend = input('input your backend:')
         ha_find = haproxy_find(backend)
         print(backend)
         for i in ha_find:
             print(i)
    elif your_choise == '2':
        add_find = input('input your backend:')
        addend = haproxy_add(add_find)
        print('\033[1;31m添加成功！\033[0m')
    elif your_choise == '3':
        ha_up =  input('input your backend:')
        haup= haproxy_update(ha_up)
        print('\033[1;31m更新成功！\033[0m')
    elif your_choise == '4':
        hup_del = input('input your backend:')
        hupdel = haproxy_delete(hup_del)
        print('\033[1;31m删除成功！\033[0m')
    elif your_choise == '5':
        exit('退出！')
    else:
        print('\033[1;31m输入错误，请重新输入！\033[0m')


