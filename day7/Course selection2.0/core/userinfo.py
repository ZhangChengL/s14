#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import pickle
class File_operate(object):
    def __init__(self):
        pass
    def file_save(self,db_name,db_path,date_info):
        db_file='%s/%s'%(db_path,db_name)
        if os.path.isfile(db_file) is not True:
            with open(db_file,'wb') as f:
                date=pickle.dump(date_info,f)
                print('\033[1;31m保存成功！\033[0m')
                return True
        else:
            print('\033[1;31m已存在！\033[0m')

    def file_open(self,db_name,db_path):
        #date=[]
        db_file = '%s/%s' % (db_path, db_name)
        if os.path.isfile(db_file):
            with open(db_file,'rb') as f:
                date=pickle.load(f)
                return date

    def file_find(self,db_path):
        choise={}
        for index,i in enumerate(os.listdir(db_path)):
            print(index,i)
            choise[index]= i
        return choise
    def file_all(self,to_find,for_find,db_path):
        choise = {}
        for index,i in enumerate(os.listdir(db_path)):
            print(index,i)
            db_file=os.path.join(db_path,i)
            with open(db_file,'rb') as f:
                file_dict= pickle.load(f)
                if file_dict[to_find]== for_find:
                    choise[index]=file_dict
        return choise

