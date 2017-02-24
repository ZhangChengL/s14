#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
from core import auth
from conf import set
from core import logger
from core import userinfo
from core import transactions

import time
import re
import logging
import os
#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')
admin_logger = logger.logger('admin')
user_date = {
    'acc_id':None,
    'is_auth':False,
    'acc_date':None,
}

admin_lg_auth = {
    'admin_auth':False
}

def user_chois(user_date):

    user_menu='''
    --------Welcome--------
    1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 交易流水
    6. 修改密码
    7. 退出
    '''
    user_menu_dict ={
        '1':user_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':transactions_log,
        '6':user_passwd_reset,
        '7':login_out
    }
    while True:
        print(user_menu)
        user_chois_into=input('请选择>>>:').strip()
        if user_chois_into in user_menu_dict:
            user_menu_dict[user_chois_into](user_date)

def admin_choise():
    admin_menu='''
    --------Welcome--------
    1. 添加账户
    2. 调整额度
    3. 冻结账户
    4. 重置密码
    5. 退出
    '''

    admin_menu_dict ={
        '1':user_add,
        '2':readjust_the_quota,
        '3':freeze_account,
        '4':admin_passwd_reset,
        '5':admin_login_out
    }
    while True:
        print(admin_menu)
        admin_choise_into=input('请选择>>>:').strip()
        if admin_choise_into in admin_menu_dict:
            admin_menu_dict[admin_choise_into]()

def userrun():
    acc_date=auth.acc_login(user_date,access_logger)
    if user_date['is_auth'] ==True:
        user_date['acc_date']=acc_date
        user_chois(user_date)

def adminrun():
    admin_auth=auth.admin_login(admin_lg_auth,admin_logger)
    if admin_auth['admin_auth'] == True:
        admin_choise()





def is_auth(func):
    def deco(*args,**kwargs):
        if user_date['is_auth']==True:
            func(*args,**kwargs)
    return deco()

def admin_is_auth(func):
    def admin_deco(*args,**kwargs):
        if admin_lg_auth['admin_auth']==True:
            func(*args,**kwargs)
    return admin_deco()




@is_auth
def user_info(acc_date):
    '''
    展示用户信息
    :return:
    '''
    acc_date_now = userinfo.load_info(acc_date['acc_id'])
    print(acc_date_now)

@is_auth
def repay(acc_date):
    '''
    还款接口
    :return:
    '''
    acc_date_now=userinfo.load_info(acc_date['acc_id'])
    repay_money=input('请输入还款金额>>>:').strip()
    if len(repay_money) > 0 and repay_money.isdigit():
        new_money=transactions.money_change(acc_date_now,'repay',repay_money,trans_logger)
        if new_money:
            print('余额为：%s'%new_money['money'])
    else:
        print('输入错误！')


@is_auth
def withdraw(acc_date):
    '''
    取款接口
    :return:
    '''
    acc_date_now = userinfo.load_info(acc_date['acc_id'])
    withdraw_money = input('请输入取款金额>>>:').strip()
    if len(withdraw_money) > 0 and withdraw_money.isdigit():
        new_money = transactions.money_change(acc_date_now, 'withdraw', withdraw_money, trans_logger)
        if new_money:
            print('余额为：%s' % new_money['money'])
    else:
        print('输入错误！')

@is_auth
def transfer(acc_date):
    '''
    转账接口
    :return:
    '''
    acc_date_now = userinfo.load_info(acc_date['acc_id'])
    transfer_id = input('请输入需要转款ID>>>:').strip()
    acc_date_tran= userinfo.load_info(transfer_id)
    if acc_date_tran:
        tran_money = input('请输入转款金额>>>:').strip()
        if len(tran_money) > 0 and tran_money.isdigit():
            new_money = transactions.money_change(acc_date_now, 'transfer', tran_money,trans_logger)
            if new_money:
                print('余额为：%s' % new_money['money'])
                tran_money = float(tran_money)
                acc_date_tran['money'] = acc_date_tran['money']+tran_money
                userinfo.dump_info(acc_date_tran)
        else:
            print('输入错误！')
    else:
        print('未查询到转款ID，请重新确认！')

@is_auth
def transactions_log(acc_date):
    '''
    交易流水接口
    :return:
    '''
    log_file='%s/log/transactions.log' %set.BASE_DIR
    to_find='user:%s' %acc_date['acc_id']
    print(to_find)
    with open(log_file,'r') as f:
        for i in f:
            if re.search(to_find,i) is not None:
                print(' '.join(i.split()))

@is_auth
def user_passwd_reset(acc_date):
    '''
    用户修改自己的账户密码
    :return:
    '''
    acc_date_now = userinfo.load_info(acc_date['acc_id'])
    new_passwd = input('请输入新密码>>>:').strip()
    acc_date_now['password'] = new_passwd
    userinfo.dump_info(acc_date_now)
    print('密码修改成功！')

def login_out(acc_date):
    '''
    退出
    :return:
    '''
    exit()

def admin_login_out():
    '''
    退出
    :return:
    '''
    exit()

@admin_is_auth
def user_add():
    '''
    管理员添加账户
    :return:
    '''
    user_add_id=input('请需要创建的用户ID>>>:')
    userinfo.admin_dump_info(user_add_id,admin_logger)

@admin_is_auth
def readjust_the_quota():
    '''
    管理员调整用户额度
    :return:
    '''
    user_up_id = input('请需要创建的用户ID>>>:').strip()
    acc_update=userinfo.load_info(user_up_id)
    if acc_update:
        new_credit=input('请输入新额度>>>:').strip()
        if len(new_credit) > 0 and new_credit.isdigit():
            acc_update['credit']=new_credit
            userinfo.dump_info(acc_update)
            admin_logger.info('user: %s credit is update!'%user_up_id)
        else:
            print('输入错误！')
    else:
        print('用户不存在！请确认后输入！')

@admin_is_auth
def freeze_account():
    '''
    管理员冻结用户账户
    :return:
    '''
    user_up_id = input('请需要创建的用户ID>>>:').strip()
    acc_update = userinfo.load_info(user_up_id)
    if acc_update:
        acc_update['status']=1
        userinfo.dump_info(acc_update)
        admin_logger.info('user: %s has been frozen!' % user_up_id)
    else:
        print('用户不存在！请确认后输入！')

@admin_is_auth
def admin_passwd_reset():
    '''
    管理员重置用户密码
    :return:
    '''
    user_up_id = input('请需要创建的用户ID>>>:').strip()
    acc_update = userinfo.load_info(user_up_id)
    if acc_update:
        acc_update['password'] = 'abc'
        userinfo.dump_info(acc_update)
        admin_logger.info('user: %s Password has been initialized!' % user_up_id)
    else:
        print('用户不存在！请确认后输入！')






