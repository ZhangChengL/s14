#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
from conf import setting
from core.userinfo import User_info
class Admin_manage(object):
    def __init__(self):
        pass
    def menu(self):
        admin_mune = '''
        \033[1;31m
        ---------Welcome----------
        1. 创建用户
        2. 修改用户密码
        3. 退出\033[0m
        '''
        admin_dict={
            '1':Admin_manage.create_user,
            '2':Admin_manage.update_passwd,
            '3':'loginout'
        }
        while True:
            print(admin_mune)
            login_choise=input('请选择>>>>').strip()
            if login_choise in admin_dict:
                if int(login_choise) == 3:
                    exit()
                else:
                    admin_dict[login_choise](self)


    def create_user(self):
        '''
        创建普通用户
        :return:
        '''
        user_acc=input('请输入用户名>>>:')
        acc_data = {
            'account' :user_acc,
            'passwd':setting.Default_password
        }
        admin_obj = User_info(user_acc,acc_data)
        admin_dump = admin_obj.dump_info()
        if admin_dump:
            print('创建成功！')


    def update_passwd(self):
        '''
        修改普通用户密码
        :return:
        '''
        user_acc = input('请输入用户名>>>:')
        acc_data = None
        admin_obj = User_info(user_acc, acc_data)
        admin_load = admin_obj.load_info()
        if admin_load:
            new_passwd = input('请输入新密码>>>:')
            admin_load['passwd'] = new_passwd
            update_obj = User_info(user_acc, admin_load)
            update_dump = update_obj.update_info()
            if update_dump:
                print('修改成功！')

