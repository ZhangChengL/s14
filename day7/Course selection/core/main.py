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