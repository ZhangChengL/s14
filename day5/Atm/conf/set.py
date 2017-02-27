#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_TYPE = {
    'transaction': 'transactions.log',  # 交易记录
    'access': 'access.log',  # 登录日志
    'admin':'admin.log'
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},#还款
    'withdraw':{'action':'minus', 'interest':0.05},#取款
    'transfer':{'action':'minus', 'interest':0.05},#转款
    'consume':{'action':'minus', 'interest':0},#购物

}

DATABASE = "%s/db/accounts" % BASE_DIR

SHOP_DATABASE = "%s/db/shop_acc" %BASE_DIR

SHOP_RE_DATABASE="%s/db/shopre"%BASE_DIR

BD_GOODS="%s/db/goods/by_good.txt"%BASE_DIR
ADMIN ={
    'account':'admin',
    'password':'admin'
}
