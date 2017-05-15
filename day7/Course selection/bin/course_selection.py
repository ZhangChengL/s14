#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from core import main

# class user(object):
#     def __init__(self):
#         pass
#     def user_choise(self):
#         choise_mune='''\033[1;31m
#         ---------Welcome----------
#         1. 学员登录
#         2. 讲师登录
#         3. 管理员登录
#         4. 退出\033[0m
#         '''
#         while True:
#             print(choise_mune)
#             login_choise=input('请选择>>>>')
#             if login_choise == '1':
#                 Student_manage()
#             elif login_choise == '2':
#                 main.Teacher_manage()
#             elif login_choise == '3':
#                 main.Admin_manage()
#             elif login_choise == '4':
#                 exit()
#             else:
#                 print('\033[1;31m输入错误！！\033[0m')



if __name__ == '__main__':
    obj = main.User()
    obj.user_choise()