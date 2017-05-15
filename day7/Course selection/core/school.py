#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from core.course import Course
from core.class_c import Class
from core.teacher import Teacher
from core.student import Student
class School(object):
    '''学校类，包含名称，地址，课程，班级，教师'''
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}             #学校所有的课程实例    {"课程名“：课程实例}
        self.school_class = {}
        self.school_teacher = {}    #类型与course一致

    def create_course(self,course_name,course_price,course_time):
        '''创建课程'''
        course_obj = Course(course_name,course_price,course_time)
        self.school_course[course_name] = course_obj

    def create_class(self,class_name,courese_obj):
        '''创建班级'''
        class_obj=Class(class_name,courese_obj)
        self.school_class[class_name]=class_obj

    def create_teacher(self,teacher_name, teacher_salary,class_name,class_obj):
        '''创建讲师'''
        teacher_obj = Teacher(teacher_name, teacher_salary)
        teacher_obj.teacher_add_class(class_name,class_obj)
        self.school_teacher[teacher_name] = teacher_obj

    def create_student(self, student_name, student_age, class_choice):
        '''注册学生'''
        student_obj = Student(student_name, student_age)  # 生成学生实例
        class_obj = self.school_class[class_choice]  # 获取学生所注册班级的实例对象
        class_obj.class_student[student_name] = student_obj  # 班级实例里添加学生信息
        self.school_class[class_choice] = class_obj  # 学校班级字典更新