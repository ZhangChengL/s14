#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl


def studentrun(student_date):
    student_menu='''
    --------Welcome--------
    1.注册
    2.登录
    3.选择课程
    4.退出

    '''
    student_menu_dict={
        '1':student_register,
        '2':student_login,
        '3':student_course_choice,
        '4':login_out
    }
    while True:
        print(student_menu)
        student_chois_into=input('请选择>>>:').strip()
        if student_chois_into in student_menu_dict:
            student_menu_dict[student_chois_into](student_date)


def teacherrun(student_date):
    student_menu='''
    --------Welcome--------
    1.注册
    2.登录
    3.选择课程
    4.退出

    '''
    student_menu_dict={
        '1':student_register,
        '2':student_login,
        '3':student_course_choice,
        '4':login_out
    }
    while True:
        print(student_menu)
        student_chois_into=input('请选择>>>:').strip()
        if student_chois_into in student_menu_dict:
            student_menu_dict[student_chois_into](student_date)