#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os

from conf import set
from core import logger
import json
import time


def acc_login(user_date,the_log):#ATM用户登录接口
    log_time = 0
    while user_date['is_auth'] != True and log_time <3:
        account=input('account>>>:').strip()
        passwd = input('password>>>:').strip()
        db_pate=set.DATABASE
        acc_file = '%s/%s.json'%(db_pate,account)
        if os.path.isfile(acc_file):
            f = open(acc_file,'r')
            acc_date = json.load(f)
            if acc_date['password'] == passwd:
                if acc_date['status'] == 0:
                    expires_date=time.mktime(time.strptime(acc_date['expire_date'],'%Y-%m-%d'))
                    if time.time()< expires_date and acc_date['status'] == 0:
                        user_date['is_auth']= True
                        user_date['acc_id'] = account
                        return acc_date
                    else:
                        print('\033[1;31m用户状态异常，请联系管理员！\033[0m')
                        break
                else:
                    print('\033[1;31m用户状态异常，请联系管理员！\033[0m')
                    break
            else:
                print('\033[1;31m账户密码错误！请重新输入！\033[0m')
            log_time +=1
        else:
            print('\033[1;31m用户不存在！\033[0m')
    else:
        the_log.error('user: %s too many login attempts!' %account)
        exit()


def admin_login(admin_lg_auth,admin_logger):#ATM管理员端登录接口
    log_time = 0
    while admin_lg_auth['admin_auth'] != True and log_time < 3:
        adminacc=input('请输入管理员账户>>>:').strip()
        adminpasswd=input('请输入管理员密码>>>:').strip()
        admin_date=set.ADMIN
        if adminacc == admin_date['account'] and adminpasswd == admin_date['password']:
            admin_lg_auth['admin_auth']=True
            admin_logger.info('admin login success!')
            return admin_lg_auth
        else:
            admin_logger.error('password is error')
    else:
        admin_logger.error('admin too many login attempts!')
        exit()


def shop_login(user_date):#购物端登录接口
    log_time= 0
    while log_time < 3:
        user_id=input('输入用户名>>>:').strip()
        user_ps=input('请输入密码>>>:').strip()
        db_path=set.SHOP_DATABASE
        user_file= '%s/%s.json'%(db_path,user_id)
        if os.path.isfile(user_file):
            f = open(user_file, 'r')
            acc_date = json.load(f)
            if acc_date['password'] == user_ps:
                user_date[ 'user_id']=user_id
                user_date['by_id']=acc_date['atmID']
                return user_date
            else:
                print('\033[1;31m密码错误！\033[0m')
                log_time=log_time+1
        else:
            print('\033[1;31m用户不存在！请确认后登录！\033[0m')
    else:
        print('\033[1;31m连续输入密码错误3次，强制退出！\033[0m')
