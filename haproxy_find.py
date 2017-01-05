#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import json
import os
import shutil
CONF_FILE = "haproxy.txt"
CONF_FILE_NEW ="haproxy_new.txt"
CONF_FILE_BAK = "haproxy_bak.txt"
CONF_FILE_TMP = "haproxy_tmp.txt"
path_exis =os.path.exists(CONF_FILE)
if path_exis == False:
    exit('配置文件不存在，强制退出')
def bak():#文件备份修改
    path_exis = os.path.exists(CONF_FILE_BAK)
    if path_exis == True:
        os.remove(CONF_FILE_BAK)
    path_exis = os.path.exists(CONF_FILE_TMP)
    if path_exis == True:
        os.remove(CONF_FILE_TMP)
    shutil.copy(CONF_FILE, CONF_FILE_BAK)
    os.rename(CONF_FILE, CONF_FILE_TMP)
    os.rename(CONF_FILE_NEW, CONF_FILE)
    os.remove(CONF_FILE_TMP)
def file_update():#文件调用
    hup_old = open(CONF_FILE,'r')
    hup_old_exis = open(CONF_FILE,'r')
    hup_new = open(CONF_FILE_NEW,'w')
    return  hup_old,hup_old_exis,hup_new
def your_input(arg):#用户输入
    yourserver = input('input server:')
    yourweight = input('input weight:')
    yourmaxconn = input('input maxconn:')
    ipaddr=yourserver.strip().split('.')
    if len(ipaddr)!=4:
        exit('IP地址输入错误！')
    for i in range(4):
        if ipaddr[i].isdigit() == False:
            exit('IP地址输入错误！')
        if int(ipaddr[i])<0 or int(ipaddr[i])>255:
            exit('IP地址输入错误！')
    if yourweight.isdigit() == False:
        exit('weight参数配置错误！请输入纯数字！')
    if yourmaxconn.isdigit() == False:
        exit('maxconn参数配置错误！请输入纯数字！')
    back = ['backend']
    ser = ['server', 'weight', 'maxconn']
    back.append(arg)
    ser.insert(ser.index('server') + 1, yourserver)
    ser.insert(ser.index('weight') + 1, yourweight)
    ser.insert(ser.index('maxconn') + 1, yourmaxconn)
    dell = ' '
    yourback=dell.join(back)+'\n'
    your_server=dell.join(ser)+'\n'
    your_servers=your_server.rjust(len(your_server)+8)
    return yourback,your_servers
def haproxy_find(arg):#查找
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
def haproxy_add(arg):#添加
    ha = False
    hadd = open('haproxy.txt','r+',encoding='utf-8')
    for x in hadd:
        if x.strip() == 'backend %s' %arg:
            ha = True
    if ha == True:
        add_choise=input('\033[1;31mbackend信息已存在，继续操作将更新backend信息！请选择是否继续y/n:\033[0m')
        if add_choise == 'y'or add_choise == 'Y':
            hadd.close()
            hap_add_upp=haproxy_update(arg)
        else:
            exit('已退出！')
    if ha == False:
        #print('没匹配到，新增')
        yourback, your_server = your_input(arg)
        hadd.write(yourback)
        hadd.write(your_server)
        hadd.close()
def haproxy_delete(arg):#删除
    hup_del, hup_del_exis, hup_del_new =file_update()
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
    bak()
def haproxy_update(arg):#更新
    hup,  hup_add_exis,hup_new = file_update()
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
            yourback, your_server=your_input(arg)
            hup_new.write(yourback)
            hup_new.write(your_server)
            continue
        hup_new.write(c)
    hup_new.close()
    hup.close()
    hup_add_exis.close()
    bak()
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


