#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import pickle
from conf import setting
from core import main
from core.userinfo import File_operate

class User_login(object):
    def __init__(self,account,passwd,user_date):
        self.account=account
        self.passwd=passwd
        self.user_date=user_date


    def student_and_teacher_login(self):
            db_path=setting.DB_LOGIN
            acc_file='%s/%s'%(db_path,self.account)
            if os.path.isfile(acc_file):
                f = open(acc_file, 'rb')
                acc_date = pickle.load(f)
                if acc_date['password'] == self.passwd:
                    self.user_date['acc_name']=acc_date['acc_name']
                    self.user_date['is_auth'] = True
                    return self.user_date
                else:
                    print('\033[1;31m账户密码错误！\033[0m')
                    return False


            else:
                print('\033[1;31m用户不存在！\033[0m')



    def admin_login(self):

            if self.account==setting.ADMIN['account'] and self.passwd == setting.ADMIN['passwd']:
                return  True
            else:
                print('\033[1;31m账户密码错误！\033[0m')





