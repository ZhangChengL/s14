#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import re
from conf import setting
from core import  main
class Student_manage(object):
    def __init__(self):
        pass

    def menu(self):
        menu_list = '''
                \033[32;1m
                 ------- 欢迎进入学生视图 ---------
                    1.选择课程
                    2.查看已选择课程
                    3.查看课程成绩
                    4.修改密码
                    5.退出
                    \033[0m
                '''
        menu_dict = {
            '1': Student_manage.choise_course,
            '2': Student_manage.show_course,
            '3': Student_manage.show_grade,
            '4': Student_manage.update_passwd,
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
    def choise_course(self):
        st_loginfo=self.file_open(main.user_date['acc_name'],setting.DB_LOGIN)
        st_usinfo=self.file_open(st_loginfo['user_name'],setting.DB_STUDENT)
        course_date = self.file_find(setting.DB_COURSE)
        course_choise = input('选择课程：')
        course_use = course_date[int(course_choise)]
        class_date =self.file_all('课程',course_use,setting.DB_CLASSES)
        class_choise = input('选择班级：')
        class_use = class_date[int(class_choise)]
        course_open=self.file_open(course_use,setting.DB_COURSE)
        course_money=course_open['价格']
        print('你需要支付%s元' %course_money)
        your_money=input('请输入金额：')
        if int(your_money)==int(course_money):
            st_add_course=[]
            #st_add_course['课程名']=course_use
            #st_add_course['班级名']=class_use['班级']
            if st_usinfo['课程']==None:
                st_add_course.append(class_use['班级'])
                st_usinfo['课程']=st_add_course
                self.file_update(st_usinfo['姓名'],setting.DB_STUDENT,st_usinfo)
            else:
                st_add_course = st_usinfo['课程']
                st_add_course.append(class_use['班级'])
                st_usinfo['课程'] = st_add_course
                self.file_update(st_usinfo['姓名'], setting.DB_STUDENT, st_usinfo)
        else:
            print('金额输入错误！')
    def show_course(self):
        st_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        st_usinfo = self.file_open(st_loginfo['user_name'], setting.DB_STUDENT)
        if st_usinfo['课程'] is not None:
            for i in st_usinfo['课程']:
                    print(i)
        else:
            print('Null')
    def show_grade(self):
        st_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        st_usernam=st_loginfo['user_name']
        st_grade=self.file_open(st_usernam,setting.DB_GRADE)
        if st_grade:
            for key in st_grade:
                print(key,st_grade[key])
        else:
            print('Null')
    def update_passwd(self):
        st_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        new_passwd=input('请输入新密码：')
        st_loginfo['password']=new_passwd
        self.file_update(main.user_date['acc_name'], setting.DB_LOGIN,st_loginfo)
    def create_student(self):
        student_dict = {}
        student_login_dict={}
        st_login_name=input('登录名：')
        st_login_passwd=input('登录密码：')
        st_name=input('姓名：')
        st_sex=input('性别：')
        student_login_dict['acc_name']=st_login_name
        student_login_dict['password']=st_login_passwd
        student_login_dict['user_name']=st_name
        student_dict['姓名']=st_name
        student_dict['性别']=st_sex
        student_dict['课程']=None
        self.file_save(st_login_name,setting.DB_LOGIN,student_login_dict)
        self.file_save(st_name,setting.DB_STUDENT,student_dict)
        print('\033[1;31m保存成功！\033[0m')
