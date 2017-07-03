#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

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
                elif int(login_choise) == 1:
                    pass


    def create_user(self):
         pass

    def update_passwd(self):
        pass
