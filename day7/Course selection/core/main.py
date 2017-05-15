#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

class User(object):
    def __init__(self):
        pass
    def user_choise(self):
        choise_mune='''\033[1;31m
        ---------Welcome----------
        1. 学员登录
        2. 讲师登录
        3. 管理员登录
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



class Student_manage(object):
    def __init__(self):
        #pass
        self.studentrun()

    def studentrun(self):
        student_menu='''
        --------Welcome--------
        1.注册
        2.登录
        3.选择课程
        4.退出

        '''
        student_menu_dict={
            '1':'student_register',
            '2':'student_login',
            '3':'student_course_choice',
            '4':'login_out'
        }
        while True:
            print(student_menu)
            student_chois_into=input('请选择>>>:').strip()
            if student_chois_into in student_menu_dict:
               if hasattr(self,student_menu_dict[student_chois_into]):
                   getattr(self,student_menu_dict[student_chois_into])()

    def student_register(self):
        pass

    def student_login(self):
        pass

    def student_course_choice(self):
        pass

    def login_out(self):
        pass

class Teacher_manage(object):
    def __init__(self):
        pass
    def teacherrun(self):
        teacher_menu = '''
               --------Welcome--------
               1.注册
               2.登录
               3.选择课程
               4.退出

               '''
        teacher_menu_dict = {
            '1': 'student_register',
            '2': 'student_login',
            '3': 'student_course_choice',
            '4': 'login_out'
        }
        while True:
            print(teacher_menu)
            teacher_chois_into = input('请选择>>>:').strip()
            if teacher_chois_into in teacher_menu_dict:
                if hasattr(self, teacher_menu_dict[teacher_chois_into]):
                    getattr(self, teacher_menu_dict[teacher_chois_into])()