#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_SCHOOL = "%s/db/school" % BASE_DIR
DB_TEACHER = "%s/db/teacher" % BASE_DIR
DB_STUDENT = "%s/db/student" % BASE_DIR
DB_CLASSES = "%s/db/classes" % BASE_DIR
DB_COURSE = "%s/db/course" % BASE_DIR
DB_RECORD = "%s/db/record" % BASE_DIR
DB_GRADE = "%s/db/grade" % BASE_DIR
DB_LOGIN = "%s/db/login" % BASE_DIR

admin_info='admin'
admin_passwd='123456'

ADMIN ={
    'account':'admin',
    'passwd':'123456'
} #ATM端管理员账户以及密码

teacher_passwd='123456'