#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import pickle
import os
import sys

user_date = {
    'acc_name':None,
    'is_auth':False
}

class User(object):
    def __init__(self):
        pass
    def user_choise(self):
        choise_mune='''\033[1;31m
        ---------Welcome----------
        1. 学员视图
        2. 讲师视图
        3. 管理员视图
        4. 退出\033[0m
        '''
        while True:
            print(choise_mune)
            login_choise=input('请选择>>>>')
            if login_choise == '1':
                Student_manage()
            elif login_choise == '2':
                Teacher_manage()
            elif login_choise == '3':
                Admin_manage()
            elif login_choise == '4':
                exit()
            else:
                print('\033[1;31m输入错误！！\033[0m')


