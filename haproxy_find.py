#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
'''HAproxy配置文件操作：
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
 arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }



'''

import json
import os
import shutil
def haproxy_find(arg):
    bg = False
    cx = []
    with open('haproxy','r',encoding='utf-8') as f:
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
# backend = input('input your backend:')
# x = haproxy_find(backend)
# print(backend)
# for i in x:
#     print(i)
def haproxy_add(arg):
    ha = False
    hadd = open('haproxy','r+',encoding='utf-8')
    for x in hadd:
        if x.strip() == 'backend %s' %arg:
            ha = True
    if ha == True:
        print('匹配到了，查看server是否一样')
        hadd.close()
        hap_add_upp=haproxy_update(arg)
        #如果一样，就退出说已存在,如果不一样，就调用更新
    if ha == False:
        print('没匹配到，新增')
        yourserver = input('input server:')
        yourweight = input('input weight:')
        yourmaxconn = input('input maxconn:')
        your_new_server = '\n'+'backend'+' '+ arg +'\n'+'        '+'server'+' '+yourserver+' '+'weight'+' '+yourweight+' '+'maxconn'+' '+yourmaxconn
        hadd.write(your_new_server)
        hadd.close()
#这是新增板块的
#如果存在就删除，不存在就退出
def haproxy_delete(arg):
    hup_del = open('haproxy','r',encoding='utf-8')
    hup_del_exis = open('haproxy','r',encoding='utf-8')
    hup_del_new = open('haproxy_new','w',encoding='utf-8')
    hup_del_is = False
    hup_exis_is =False
    for hd_exis in hup_del_exis:
        if hd_exis.strip() ==  'backend %s' %arg:
            hup_exis_is = True
            break
    if hup_exis_is == False:
        exit('不存在！')
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
    os.remove('haproxy.bak')
    shutil.copy('haproxy', 'haproxy.bak')
    os.rename('haproxy', 'haproxy_tmp')
    os.rename('haproxy_new', 'haproxy')
    os.remove('haproxy_tmp')
# hup_del = input('input your backend:')
# hupdel = haproxy_delete(hup_del)
def haproxy_update(arg):
    hup = open('haproxy','r',encoding='utf-8')
    hup_new = open('haproxy_new','w',encoding='utf-8')
    hup_add_exis = open('haproxy','r',encoding='utf-8')
    hup_add_is = False
    hup_is = False
    for huadd_exis in hup_add_exis:
        if huadd_exis.strip() == 'backend %s' %arg:
            hup_add_is = True
            break
    if hup_add_is == False:
        exit('不存在！')
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
    os.remove('haproxy.bak')
    shutil.copy('haproxy','haproxy.bak')
    os.rename('haproxy','haproxy_tmp')
    os.rename('haproxy_new','haproxy')
    os.remove('haproxy_tmp')

# hap_up = input('input your backend:')
# hapup = haproxy_update(hap_up)
    #如果存在就更新，不存在就退出
meg = '''
=======================Welcome====================
1.查看backend
2.添加backend
3.更新backend
4.删除backend
5.退出



'''


add_find = input('input your backend:')
addend = haproxy_add(add_find)
