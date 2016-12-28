#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
path_exis=os.path.exists('by_acc.txt')
if path_exis == False:
    exit('文件不存在！')
acc_by_list = open('by_acc.txt','r',encoding='utf-8')
yourname= input('请输入用户名：')
yourpasswd = input('请输入密码：')
match = False
userout = False
logintime = 2
for i in acc_by_list:
    your_name,your_psswd,your_money = tuple(i.strip().split())
    if yourname == your_name:
        userout = True
        if yourpasswd == your_psswd:
            match = True
            break
        elif yourpasswd != your_psswd:
            for login_time in range(logintime):
                passwd_agin = input('密码错误，请再次输入：')
                if passwd_agin == your_psswd:
                    match = True
                    break
if userout == False:
    exit('用户不存在！')
if match == False:
    print('密码已连续输入错误%s次，强制退出' %(logintime+1))
if match == True:
    print('登录成功')
    if your_money == '0':
        yourmoney = input('你是第一次登录，请输入你的金额：')
        your_money = yourmoney
        print(your_money)
    else:
        print('欢迎再次光临！你的余额为%s' %your_money)

mes ='''
\033[1;32m
================Welcome================
1.购物
2.查询消费记录
3.退出\033[0m

'''
while True:
    print(mes)
    your_choise = input('请选择：')
    if your_choise.isdigit():
        your_choise = int(your_choise)
        if your_choise == 1:
            good = open('by_good.txt','r',encoding='utf-8').read()
            goods = eval(good)
            for index,item in enumerate(goods):
                print(index,item)
            good_by = []
            your_money = int(your_money)
            while True:
                good_id = input('输入你需要购买的商品ID，按e键可结束购买:')
                if good_id == 'e':
                    print('你本次购买的商品：\033[1;31m%s\033[0m'%good_by)
                    print('剩余余额：\033[1;31m%s\033[0m' %your_money)
                    break
                if good_id.isdigit():
                    good_id = int(good_id)
                    if good_id < len(goods) and good_id >= 0:
                        if goods[good_id][1] <= your_money:
                            good_by.append(goods[good_id])
                            your_money -= goods[good_id][1]
                            print('\033[1;34m你选择的商品%s已加入购物车\033[0m' % goods[good_id])
                        else:
                            print('\033[1;31m余额不足:%s\033[0m ' % your_money)
                    else:
                        print('\033[1;31m你输入的商品不存在，请重新输入或者按e退出\033[0m')
                else:
                    print('\033[1;31m输入错误，请输入数字或者e退出\033[0m')
        if your_choise == 2:
            print('\033[1;32m你的历史消费记录：\033[0m')
            record_c = open('by_record.txt', 'r', encoding='utf-8')
            records_c = eval(record_c.read())
            print(records_c.get(yourname))
            record_c.close()
        if your_choise == 3:
            print('\033[1;32m欢迎下次光临！\033[0m')
            break

    else:
        print('\033[1;31m输入错误请重新输入!!\033[0m')
by_acc_new = open('by_acc_new.txt', 'w')
by_acc_old = open('by_acc.txt','r')
for c in by_acc_old:
    yn,yp,ym=tuple(c.strip().split())
    if yn == yourname:
        acc_new = yourname + ' ' + yourpasswd + ' ' + str(your_money)+'\n'
        by_acc_new.write(acc_new)
    else:
        by_acc_new.write(c)
by_acc_new.close()
by_acc_old.close()
acc_by_list.close()
os.rename('by_acc.txt', 'by_acc_tmp.txt')
os.rename('by_acc_new.txt', 'by_acc.txt')
os.remove('by_acc_tmp.txt')