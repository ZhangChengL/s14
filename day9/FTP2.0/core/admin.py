#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import hashlib
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
        3. 修改磁盘配额
        4. 退出\033[0m
        '''
        admin_dict={
            '1':Admin_manage.create_user,
            '2':Admin_manage.update_passwd,
            '3':Admin_manage.update_space,
            '4':'loginout'
        }
        while True:
            print(admin_mune)
            login_choise=input('请选择>>>>').strip()
            if login_choise in admin_dict:
                if int(login_choise) == 4:
                    exit()
                else:
                    admin_dict[login_choise](self)


    def create_user(self):
        '''
        创建普通用户
        :return:
        '''
        user_acc=input('请输入用户名>>>:')
        user_space = input('请输入磁盘配额（M）>>>:')
        user_space = int(user_space)*1024*1024
        hash = hashlib.md5()
        hash.update(setting.Default_password.encode())
        md5_passwd=hash.hexdigest()
        acc_data = {
            'account' :user_acc,
            'passwd':md5_passwd,
            'space':user_space
        }
        admin_obj = User_info(user_acc,acc_data)#调用信息存放接口
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
        admin_obj = User_info(user_acc, acc_data) #调用信息读取接口，获取用户信息
        admin_load = admin_obj.load_info()
        if admin_load:
            new_passwd = input('请输入新密码>>>:')
            hash = hashlib.md5()
            hash.update(new_passwd.encode())
            md5_passwd = hash.hexdigest()
            admin_load['passwd'] = md5_passwd
            update_obj = User_info(user_acc, admin_load) #调用信息存放接口
            update_dump = update_obj.update_info()
            if update_dump:
                print('修改成功！')

    def update_space(self):
        '''
        修改用户磁盘空间配额
        :return:
        '''
        user_acc = input('请输入用户名>>>:')
        acc_data = None
        admin_obj = User_info(user_acc, acc_data)  # 调用信息读取接口，获取用户信息
        admin_load = admin_obj.load_info()
        if admin_load:
            new_space = input('请输入新的磁盘配额：')
            if int(new_space) >= int(admin_load['space']):
                admin_load['space'] = new_space
                update_obj = User_info(user_acc,admin_load)
                update_dump = update_obj.update_info()
                if update_dump:
                    print('修改成功！')
            else:
                print('\033[1;31m新的磁盘空间大小不能小于预设磁盘空间大小！\033[0m')