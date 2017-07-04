#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import json
import os
from conf import setting
class User_info(object):
    def __init__(self,account,acc_date):
        self.account = account
        self.acc_date = acc_date
    def dump_info(self):
        '''
        新建用户创建信息接口
        :return:
        '''
        user_path = setting.USER_INFO_PATH
        user_file = os.path.join(user_path,self.account)
        file_path = setting.USER_FILE_PATH
        user_file_path = os.path.join(file_path,self.account)
        if os.path.isfile(user_file) is not True:
            with open(user_file,'w') as f:
                user_date = json.dump(self.acc_date,f)
            os.mkdir(user_file_path)
            return True
        else:
            print('\033[1;31m用户已存在！请确认后重新创建\033[0m')
    def load_info(self):
        '''
        获取用户账户信息接口
        :return:
        '''
        user_path = setting.USER_INFO_PATH
        user_file = os.path.join(user_path, self.account)
        if os.path.isfile(user_file):
            with open(user_file) as f:
                acc_data = json.load(f)
                return acc_data

    def update_info(self):
        '''
        更新用户信息接口
        :return:
        '''
        user_path = setting.USER_INFO_PATH
        user_file = os.path.join(user_path, self.account)
        if os.path.isfile(user_file):
            with open(user_file,'w') as f:
                user_date = json.dump(self.acc_date,f)
            return True

