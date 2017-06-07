#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
from conf import setting
class Student_manage(object):
    def __init__(self):
        pass

    def menu(self):
        menu_list = '''
                \033[32;1m
                 ------- 欢迎进入学生视图 ---------
                    1.
                    2.
                    3.
                    4.
                    5.  退出
                    \033[0m
                '''
        menu_dict = {
            '1': Student_manage.create_course,
            '2': Student_manage.create_classes,
            '3': Student_manage.create_teacher,
            '4': Student_manage.create_school,
            '5': 'exit'
        }
        while True:
            print(menu_list)
            choise = input('请选择>>>:').strip()
            if choise in menu_dict:
                if choise == '5':
                    exit()
                else:
                    menu_dict[choise](self)

    def create_student(self):
        student_dict = {}
        student_login_dict={}
        st_login_name=input('登录名：')
        st_login_passwd=input('登录密码：')
        st_name=input('姓名：')
        st_sex=input('性别：')
        student_login_dict['acc_name']=st_login_name
        student_login_dict['passwd']=st_login_passwd
        student_dict['姓名']=st_name
        student_dict['性别']=st_sex
        self.file_save(st_login_name,setting.DB_LOGIN,student_login_dict)
        self.file_save(st_name,setting.DB_STUDENT,student_dict)