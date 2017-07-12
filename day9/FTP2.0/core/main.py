#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import json
from core.auth import Login_auth
from core.admin import Admin_manage
from core.user import User_manage
user_info = None
class User(object):
    def __init__(self):
        pass
    def user_choise(self):
        '''
        程序主界面
        :return:
        '''
        choise_menu = '''
        \033[1;31m
        ---------Welcome----------
        1. 普通用户登录
        2. 管理员登录
        3. 退出\033[0m
        '''
        menu_dict={
            '1':User_manage,
            '2':Admin_manage,
            '3':'loginout'
        }
        while True:
            print(choise_menu)
            login_choise=input('请选择>>>>').strip()
            if login_choise in menu_dict:
                if int(login_choise) == 3:
                    exit()
                elif  int(login_choise) ==2:
                    username = input('请输入用户名>>>').strip()
                    passwd = input('请输入密码>>>').strip()
                    admin_obj = Login_auth(username, passwd, user_info) #调用管理员认证接口
                    admin_into = admin_obj.admin_login()
                    if admin_into:
                        menu_dict[login_choise].menu(self) #调用管理员主界面
                elif int(login_choise) == 1:
                    username = input('请输入用户名>>>').strip()
                    passwd = input('请输入密码>>>').strip()
                    user_obj = Login_auth(username, passwd, user_info) #调用普通用户认证接口
                    user_login = user_obj.user_login()
                    if user_login:
                        print('\033[1;31m登录成功！！\033[0m')
                        user_obj=menu_dict[login_choise](user_login) #调用ftp客户端
                        user_client = user_obj.server_client()
            else:
                print('\033[1;31m输入错误！！\033[0m')