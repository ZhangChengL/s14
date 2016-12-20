#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
acc = open('acc','r',encoding='utf-8')
black = open('black','r+',encoding='utf-8')
while True:
    yourname = input('请输入用户名：')
    for black_list in black:
        black_list = black_list.strip()
        if yourname == black_list:
            print('用户已锁定，退出！')
            exit()
    match = False
    userout = False
    for i in acc:
        user,password = i.strip().split()
        if user== yourname:
            userout = True
            passwd = input('请输入密码：')
            if password == passwd:
                match = True
                break
            elif password != passwd:
                for login in range(2):
                    passwd = input('密码错误，请再次输入：')
                    if passwd == password:
                        match = True
                        break
    if userout == False:
         print('用户不存在，退出！')
         exit()
    elif match == False:
         print('已输入密码3次，用户已锁定，暂时无法登录！')
         black.write('\n %s' %yourname)
         black.close()
         exit()
    elif match == True:
          print('登录成功！')
          exit()
