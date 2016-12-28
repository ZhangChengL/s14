#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#acc文件存放用户账户和密码，byacc存放用户金额，good文件存放商品列表，record存放购物记录
import os
import sys
acc_mon = open('byacc','r+')
acc = open('acc.txt','r',encoding='utf-8')
yourname = input('输入用户名：')
password = input('输入密码：')
match = False
userout = False
money_out= False
for i in acc:
    user,passwd = i.strip().split()
    if user == yourname:
        userout = True
        if password == passwd:
            match = True
            break
        elif password != passwd:
            for login in range(2):
                passwd_agin = input('密码错误，请再次输入：')
                if passwd_agin == passwd:
                    match = True
                    break
if userout == False:
    print('用户不存在，退出')
    exit()
if match == False:
    print('密码已错误3次，强制退出')
    exit()
if match == True:
    print('登录成功！')
    #print('\033[1;32mWelcome to shopping!\033[0m')
    #pass
for j in acc_mon:
    by_acc,by_money = j.strip().split()
    if yourname == by_acc:
        money_out = True
        #print('尊敬的顾客，你的余额为：\033[1;31m%s\033[0m' %by_money)
        break
if money_out == False:
    youmoney = input('第一次登录，请输入金额：')
    your_acc_money = '\n' + yourname +' '+youmoney
    acc_mon.write(your_acc_money)
    print('金额录入成功，你的余额为：\033[1;31m%s\033[0m' %youmoney)
    acc_mon.close()
acc_mons = open('byacc','r+')
for x in acc_mons:
    by_accs,by_moneys = tuple(x.strip().split())
    if yourname == by_accs:
        print('尊敬的顾客，你的余额为：\033[1;31m%s\033[0m' % by_moneys)
        yourname = by_accs
        youmoney = by_moneys
#print(yourname,youmoney)

print('\033[1;32m================Welcome================\033[0m')
mes ='''
\033[1;32m1.购物
2.查询消费记录
3.退出\033[0m

'''

while True:
    print(mes)
    choice =input('请选择：')

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            good = open('good','r',encoding='utf-8').read()
            goods = eval(good)
            for index,item in enumerate(goods):
                print(index,item)
            good_by = []
            user_by = {}
            yourmoneys = int(youmoney)
            while True:
                good_id = input('输入你需要购买的商品ID，按e键可结束购买:')
                if good_id == 'e':
                    print('你本次购买的商品：\033[1;31m%s\033[0m'%good_by)
                    print('剩余余额：\033[1;31m%s\033[0m' %yourmoneys)
                    break
                if good_id.isdigit():
                    good_id = int(good_id)
                    if good_id < len(goods) and good_id >=0:
                        if goods[good_id][1] <= yourmoneys:
                            good_by.append(goods[good_id])
                            yourmoneys -= goods[good_id][1]
                            print('\033[1;34m你选择的商品%s已加入购物车\033[0m' %goods[good_id])
                        else:
                            print('\033[1;31m余额不足:%s\033[0m ' %yourmoneys)
                    else:
                        print('\033[1;31m你输入的商品不存在，请重新输入或者按e退出\033[0m')
                else:
                    print('\033[1;31m输入错误，请输入数字或者e退出\033[0m')
            record = open('record', 'r+', encoding='utf-8')
            records = eval(record.read())
            good_old=records.get(yourname)
            good_by.append(good_old)
            user_by.setdefault(yourname,good_by)
            records.update(user_by)
            records_str = str(records)
            record_w = open('record','w',encoding='utf-8')
            record_w.writelines(records_str)  #追加消费记录
            record.close()
            record_w.close()
        if choice == 2:
            print('\033[1;32m你的历史消费记录：\033[0m')
            record_c = open('record', 'r+', encoding='utf-8').read()
            records_c = eval(record_c)
            print(records_c.get(yourname))  #查询消费记录
        if choice == 3:
            print('\033[1;32m欢迎下次光临！\033[0m')
            break
    else:
        print('\033[1;31m输入错误请重新输入!!\033[0m')
acc_mon_new = open('byacc_new', 'w')
acc_mon_old = open('byacc', 'r')
for c in acc_mon_old:
    if c.strip().startswith(yourname):
        acc_new = yourname + ' ' + str(yourmoneys) + '\n'
        acc_mon_new.write(acc_new)
    else:
        acc_mon_new.write(c)
acc_mon_new.close()
acc_mon_old.close()
acc_mons.close()
acc_mon.close()
os.rename('byacc', 'byacc_tmp')
os.rename('byacc_new', 'byacc')
os.remove('byacc_tmp')
