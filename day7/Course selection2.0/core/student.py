#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

class Student_manage(object):
    def __init__(self):
        pass

    def menu(self):
        menu_list = '''
                \033[32;1m
                 ------- 欢迎进入学生视图 ---------
                    1.  创建课程
                    2.  创建班级
                    3.  创建讲师
                    4.  创建学校
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