#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import re
import pickle
import time
from conf import setting
from core import  main
class Teacher_manage(object):
    def __init__(self):
        pass

    def menu(self):
        menu_list = '''\033[32;1m
            ------- 欢迎进入教师视图 ---------
                1.查看在授班级学生列表
                2.管理学生成绩
                3.上课打卡
                4.修改密码
                5.退出\033[0m
                       '''
        menu_dict = {
            '1': Teacher_manage.show_student,
            '2': Teacher_manage.manage_grade,
            '3': Teacher_manage.clock_in,
            '4': Teacher_manage.update_passwd,
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

    def show_student(self):
        te_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        te_usinfo = self.file_open(te_loginfo['user_name'], setting.DB_TEACHER)
        teacher_name=te_usinfo['姓名']
        teacher_class=self.file_all('讲师',teacher_name,setting.DB_CLASSES)
        class_choise = input('选择班级：')
        class_use = teacher_class[int(class_choise)]
        #choise = {}
        for index,i in enumerate(os.listdir(setting.DB_STUDENT)):
            db_file=os.path.join(setting.DB_STUDENT,i)
            with open(db_file,'rb') as f:
                file_dict= pickle.load(f)
                if file_dict['课程'] is not None:
                    for x in file_dict['课程']:
                        if x == class_use['班级']:
                            #choise[index]=file_dict['姓名']
                            print(index,i)

    def manage_grade(self):
        te_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        te_usinfo = self.file_open(te_loginfo['user_name'], setting.DB_TEACHER)
        teacher_name = te_usinfo['姓名']
        teacher_class = self.file_all('讲师', teacher_name, setting.DB_CLASSES)
        class_choise = input('选择班级：')
        class_use = teacher_class[int(class_choise)]
        choise = {}
        for index, i in enumerate(os.listdir(setting.DB_STUDENT)):
            db_file = os.path.join(setting.DB_STUDENT, i)
            with open(db_file, 'rb') as f:
                file_dict = pickle.load(f)
                if file_dict['课程'] is not None:
                    for x in file_dict['课程']:
                        if x == class_use['班级']:
                            choise[index]=file_dict['姓名']
                            print(index, i)
        choise_stu=input('选择学生：')
        stu_manage=choise[int(choise_stu)]
        if self.file_open(stu_manage,setting.DB_GRADE):
            stu_grade=self.file_open(stu_manage,setting.DB_GRADE)
            new_grade=input('录入成绩：')
            stu_grade[class_use['班级']]=new_grade
            self.file_update(stu_manage,setting.DB_GRADE,stu_grade)
        else:
            stu_grade={}
            new_grade = input('录入成绩：')
            stu_grade[class_use['班级']] = new_grade
            self.file_update(stu_manage, setting.DB_GRADE, stu_grade)
    def clock_in(self):
        te_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        te_usinfo = self.file_open(te_loginfo['user_name'], setting.DB_TEACHER)
        teacher_name = te_usinfo['姓名']
        teacher_class = self.file_all('讲师', teacher_name, setting.DB_CLASSES)
        class_choise = input('选择班级：')
        class_use = teacher_class[int(class_choise)]
        if self.file_open(teacher_name,setting.DB_RECORD):
            te_record=self.file_open(teacher_name,setting.DB_RECORD)
            date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            te_record[date]=class_use
            self.file_update(teacher_name,setting.DB_RECORD,te_record)
        else:
            te_record={}
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            te_record[date] = class_use
            self.file_update(teacher_name, setting.DB_RECORD, te_record)

    def update_passwd(self):
        st_loginfo = self.file_open(main.user_date['acc_name'], setting.DB_LOGIN)
        new_passwd = input('请输入新密码：')
        st_loginfo['password'] = new_passwd
        self.file_update(main.user_date['acc_name'], setting.DB_LOGIN, st_loginfo)