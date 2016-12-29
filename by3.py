#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
import json
path_exis=os.path.exists('by_acc.txt')
if path_exis == False:
    exit('文件不存在！')
meg = '''
\033[1;32m
1.登录
2.注册
3.退出\033[0m

'''
while True:
    print(meg)
    login_choise = input('请选择：')
    if login_choise == '1':
        acc_by_list = open('by_acc.txt','r',encoding='utf-8')
        yourname= input('请输入用户名：')
        yourpasswd = input('请输入密码：')
        match = False
        userout = False
        logintime = 2
        for i in acc_by_list:
            your_name,your_psswd,your_money= tuple(i.strip().split())
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
                #print(your_money)
            else:
                print('欢迎再次光临！你的余额为%s' %your_money)

        mes ='''
        \033[1;32m
        ================Welcome================
        1.购物
        2.查询消费记录
        3.充值
        4.退出\033[0m

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
                            #更新金额
                            by_acc_new = open('by_acc_new.txt', 'w',encoding='utf-8')
                            by_acc_old = open('by_acc.txt', 'r',encoding='utf-8')
                            for c in by_acc_old:
                                if c.strip().startswith(yourname):
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
                            #更新购物记录
                            yourrecordup = open('by_record.txt', 'r', encoding='utf-8')
                            yourrecord_up=yourrecordup.read()
                            your_record_up= eval(yourrecord_up)
                            isup= False
                            for is_up in your_record_up:
                                if is_up == yourname:
                                    isup=True
                                    break
                            if isup == True:
                                #print('存在，就更新')
                                your_records_up = eval(str(your_record_up.get(yourname)))
                                your_records_up.extend(good_by)
                                by_record_new = open('by_record_new.txt', 'w', encoding='utf-8')
                                your_record_up[yourname] = your_records_up
                                by_record_new.write(str(your_record_up))
                                yourrecordup.close()
                                by_record_new.close()
                                os.rename('by_record.txt','by_record_tmp.txt')
                                os.rename('by_record_new.txt','by_record.txt')
                                os.remove('by_record_tmp.txt')
                            yourrecordup.close()
                            if isup ==False:
                                #print('不存在，就新增')
                                yourrecordadd = open('by_record.txt', 'r', encoding='utf-8')
                                yourrecord_add = yourrecordadd.read()
                                your_record_add = eval(yourrecord_add)
                                your_record_add[yourname] =good_by
                                #print(your_record_up)
                                by_record_new_add = open('by_record_new.txt', 'w', encoding='utf-8')
                                by_record_new_add.write(str(your_record_add))
                                yourrecordadd.close()
                                by_record_new_add.close()
                                os.rename('by_record.txt', 'by_record_tmp_add.txt')
                                os.rename('by_record_new.txt', 'by_record.txt')
                                os.remove('by_record_tmp_add.txt')
                            break
                        if good_id.isdigit():
                            good_id = int(good_id)
                            if good_id < len(goods) and good_id >= 0:
                                if goods[good_id][1] <= your_money:
                                    good_by.append(goods[good_id])
                                    your_money -= goods[good_id][1]
                                    print('\033[1;34m你选择的商品%s已加入购物车\033[0m' % goods[good_id])
                                else:
                                    print('\033[1;31m余额不足,剩余金额为:%s\033[0m ' % your_money)
                            else:
                                print('\033[1;31m你输入的商品不存在，请重新输入或者按e退出\033[0m')
                        else:
                            print('\033[1;31m输入错误，请输入数字或者e退出\033[0m')
                if your_choise == 2:
                    yourrecord = open('by_record.txt','r',encoding='utf-8')
                    yourrecord_cx = yourrecord.read()
                    your_record = eval(yourrecord_cx)
                    isexis= False
                    for is_exis in your_record:
                        if is_exis == yourname:
                            isexis = True
                            break
                    if isexis == True:
                        print('\033[1;32m你的历史消费记录：\033[0m')
                        your_records=eval(str(your_record.get(yourname)))
                        for cx in your_records:
                            print(cx)
                        yourrecord.close()
                    if isexis == False:
                             print('暂无消费记录！')
                    yourrecord.close()
                if your_choise == 4:
                    print('\033[1;32m欢迎下次光临！\033[0m')
                    exit()
                if your_choise == 3:
                    your_add_money = int(input('请输入需要充值的金额：'))
                    user_money = open('by_acc.txt','r')
                    user_money_new = open('by_acc_money.txt', 'w')
                    for us in user_money:
                        us_name,us_pass,us_money = tuple(us.strip().split())
                        if us_name ==yourname:
                            us_money = int(us_money)
                            us_money = us_money + your_add_money
                            your_money = us_money
                            user_money_add = yourname + ' ' + yourpasswd + ' ' + str(us_money)+'\n'
                            user_money_new.write(user_money_add)
                        else:
                            user_money_new.write(us)
                    user_money.close()
                    user_money_new.close()
                    acc_by_list.close()
                    os.rename('by_acc.txt', 'by_acc_tmp.txt')
                    os.rename('by_acc_money.txt', 'by_acc.txt')
                    os.remove('by_acc_tmp.txt')
                    print('\033[1;31m充值成功！余额为：%s\033[0m' %your_money)

            else:
                print('\033[1;31m输入错误请重新输入!!\033[0m')
    if login_choise == '3':
        print('\033[1;32m欢迎下次光临！\033[0m')
        exit()
    if login_choise == '2':
        add_login = open('by_acc.txt','r')
        add_logins = open('by_acc_login.txt','w')
        add_name = input('请输入用户名：')
        add_pass = input('请输入登录密码：')
        add_pass_agin = input('请再次输入登录密码：')
        add_money = '0'
        if add_pass == add_pass_agin:
            for ad in add_login:
                lg_usr,lg_psaa,lg_money = tuple(ad.strip().split())
                login_usr_lod =lg_usr+' '+lg_psaa+' '+lg_money+'\n'
                add_logins.write(login_usr_lod)
            add_user =add_name + ' ' + add_pass + ' ' + add_money
            add_logins.write(add_user)
            add_login.close()
            add_logins.close()
            os.rename('by_acc.txt', 'by_acc_login_tmp.txt')
            os.rename('by_acc_login.txt', 'by_acc.txt')
            os.remove('by_acc_login_tmp.txt')
            print('\033[1;31m注册成功\033[0m')
        else:
            print('两次密码不一致，请重新注册！')
    else:
        print('输入错误！请重新输入')
