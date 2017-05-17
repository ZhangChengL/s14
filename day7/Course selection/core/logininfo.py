#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

class Student_info(object):
    '''学生账号类：账户，密码'''
    def __init__(self,st_username,st_passwd):
        self.st_username=st_username
        self.st_passwd=st_passwd

class Teacher_info(object):
    '''讲师账户类：账户，默认获取配置文件密码'''
    def __init__(self,tea_username,tea_passwd):
        self.tea_username=tea_username
        self.tea_username=tea_passwd