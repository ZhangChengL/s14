#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
from core.school import School
from core.userinfo import File_operate
from conf import setting
class Admin_manage(File_operate):
    def __init__(self):
        File_operate.__init__(self)
        #pass
    def menu(self):
        menu_list='''
        \033[32;1m
         ------- 欢迎进入管理员视图 ---------
            1.  创建课程
            2.  创建班级
            3.  创建讲师
            4.  创建学校
            5.  退出
            \033[0m
        '''
        menu_dict={
            '1':Admin_manage.create_course,
            '2':Admin_manage.create_classes,
            '3':Admin_manage.create_teacher,
            '4':Admin_manage.create_school,
            '5':'exit'
        }
        print(menu_list)
        choise = input('请选择>>>:').strip()
        if choise in menu_dict:
            if choise == '5':
                exit()
            else:
                menu_dict[choise](self)

    def create_course(self):
        course_dict={}
        course_name = input('课程名：')
        course_prices = input('价格：')
        course_period = input('周期：')
        school_date = File_operate.file_find(setting.DB_SCHOOL)
        school_choise = input('选择学校：')
        school_use = school_date[school_choise]
        course_dict['课程']=course_name
        course_dict['价格'] =course_prices
        course_dict['周期'] = course_period
        course_dict['学校'] = school_use
        File_operate.file_save(course_name,setting.DB_COURSE,course_dict)
    def create_classes(self):
        classes_dict = {}
        school_date = File_operate.file_find(setting.DB_SCHOOL)
        school_choise = input('选择学校：')
        school_use=school_date[school_choise]['校名']
        course_date = File_operate.file_all('学校',school_use,setting.DB_COURSE)
        course_choise = input('选择课程：')
        course_use = course_date[course_choise]['课程']
        teacher_date = File_operate.file_all('学校',school_use,setting.DB_TEACHER)
        teacher_choise = input('选择讲师')
        teacher_use = teacher_date[teacher_choise]['姓名']
        classes_name = input('班级名：')
        classes_dict['学校']=school_use
        classes_dict['课程']=course_use
        classes_dict['讲师']=teacher_use
        classes_dict['班级']=classes_name
        File_operate.file_save(classes_name,setting.DB_CLASSES,classes_dict)

    def create_teacher(self):
        teacher_dict ={}
        teacher_logininfo={}
        teacher_loginname=input('讲师登录用户名：')
        teacher_realname = input('讲师姓名：')
        school_choise=File_operate.file_find(setting.DB_SCHOOL)
        teacher_choise =  input('选择学校：')
        teacher_school = school_choise[teacher_choise]
        teacher_dict['姓名']=teacher_realname
        teacher_dict['学校']=teacher_school
        teacher_logininfo['用户名'] = teacher_loginname
        teacher_logininfo['密码'] = setting.teacher_passwd
        File_operate.file_save(teacher_loginname,setting.DB_LOGIN,teacher_logininfo)
        File_operate.file_save(teacher_realname,setting.DB_TEACHER,teacher_dict)

    def create_school(self):
        school_dict={}
        school_name= input('校名：')
        school_address= input('地址：')
        #sc= School(school_name,school_address)
        school_dict['校名']=school_name
        school_dict['地址']=school_address
        ff=File_operate()
        ff.file_save(school_name,setting.DB_SCHOOL,school_dict)
        #File_operate.file_save(school_name,setting.DB_SCHOOL,school_dict)
        #self.file_save(school_name,setting.DB_SCHOOL,school_dict)