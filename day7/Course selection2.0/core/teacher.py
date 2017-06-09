#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
class Teacher_manage(object):
    def __init__(self):
        pass

    def menu(self):
        menu_list = '''\033[32;1m
            ------- 欢迎进入教师视图 ---------
                1.查看信息
                2.查看在授课程学生列表
                3.管理学生成绩
                4.修改密码
                5.退出\033[0m
                       '''