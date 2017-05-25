#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import pickle
import os
import sys
from core.auth import User_login
from core.student import Student_manage
from core.teacher import Teacher_manage
from core.admin import Admin_manage
user_date = {
    'acc_name':None,
    'is_auth':False
}

class User(object):
    def __init__(self):
        pass
    def user_choise(self):
        choise_menu='''\033[1;31m
        ---------Welcome----------
        1. 学员视图
        2. 讲师视图
        3. 管理员视图
        4. 退出\033[0m
        '''
        menu_dict = {
            '1':Student_manage,
            '2':Teacher_manage,
            '3':Admin_manage,
            '4':'loginout'
        }
        while True:
            print(choise_menu)
            login_choise=input('请选择>>>>').strip()
            if login_choise in menu_dict:
                if int(login_choise) == 4:
                    exit()
                else:
                    username=input('请输入用户名>>>').strip()
                    passwd= input('请输入密码>>>').strip()
                    user_dates=user_date
                    if int(login_choise) ==3 :
                        admin_obj=User_login(username,passwd,user_dates)
                        admin_into=admin_obj.admin_login()
                        if admin_into:
                            menu_dict[login_choise].menu(self)
                    else:
                        user_obj=User_login(username,passwd,user_dates)
                        user_login=user_obj.student_and_teacher_login()
                        if user_login['is_auth'] == True:
                            menu_dict[login_choise].menu(self)
            else:
                print('\033[1;31m输入错误！！\033[0m')

            # if login_choise == '1':
            #     Student_manage()
            # elif login_choise == '2':
            #     Teacher_manage()
            # elif login_choise == '3':
            #     Admin_manage()
            # elif login_choise == '4':
            #     exit()
            # else:
            #     print('\033[1;31m输入错误！！\033[0m')

