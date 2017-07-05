#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import json
from conf import setting

class Login_auth(object):
    def __init__(self,account,passwd,user_info):
        '''
        :param account:
        :param passwd:
        :param user_info:
        '''
        self.account = account
        self.passwd = passwd
        self.user_info = user_info

    def user_login(self):
        '''
        普通用户登录验证接口
        :return:
        '''
        db_path = setting.USER_INFO_PATH
        user_file = os.path.join(db_path,self.account) #获取用户登录信息数据
        if os.path.isfile(user_file):
            f = open(user_file,'r')
            acc_date = json.load(f)
            if acc_date['passwd'] == self.passwd:
                self.user_info = acc_date['account']
                return self.user_info
            else:
                print('\033[1;31m密码错误！\033[0m')
                #return False
        else:
            print('\033[1;31m用户不存在！\033[0m')

    def admin_login(self):
        '''
        管理员登录验证接口
        :return:
        '''
        if self.account == setting.ADMIN_INFO['username'] and self.passwd == setting.ADMIN_INFO['password']:
            return  True
        else:
            print('\033[1;31m账户密码错误！\033[0m')

