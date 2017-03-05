#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
from conf import set
from core import userinfo
from core import logger
def money_change(acc_date,tr_type,change_money,tr_log):
    '''
    金额计算接口
    :param acc_date:
    :param tr_type:
    :param change_money:
    :param tr_log:
    :return:
    '''
    change_money=float(change_money)
    if tr_type in set.TRANSACTION_TYPE:
        interest = change_money * set.TRANSACTION_TYPE[tr_type]['interest']
        old_money = acc_date['money']
        if set.TRANSACTION_TYPE[tr_type]['action'] == 'plus':
            new_money = old_money + change_money + interest
        if set.TRANSACTION_TYPE[tr_type]['action'] == 'minus':
            new_money = old_money - change_money - interest
            if new_money <0:
                print('\033[1;31m余额不足！\033[0m')
                return
        acc_date['money'] = new_money
        userinfo.dump_info(acc_date)
        tr_log.info("user:%s   action:%s    money:%s   interest:%s" %(acc_date['id'], tr_type, change_money,interest))
        return acc_date
    else:
        print('\033[1;31m交易类型不存在！\033[0m')
