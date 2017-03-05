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
    'admin':'admin.log'#管理员操作日志
}#日志类型

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},#还款
    'withdraw':{'action':'minus', 'interest':0.05},#取款
    'transfer':{'action':'minus', 'interest':0.05},#转款
    'consume':{'action':'minus', 'interest':0},#购物

}  #消费类型接口

DATABASE = "%s/db/accounts" % BASE_DIR #获取银行卡用户信息存放路径

SHOP_DATABASE = "%s/db/shop_acc" %BASE_DIR #获取购物端用户存放路径

SHOP_RE_DATABASE="%s/db/shopre"%BASE_DIR #获取用户购物记录存放路径

BD_GOODS="%s/db/goods/by_good.txt"%BASE_DIR#商品列表

ADMIN ={
    'account':'admin',
    'password':'admin'
} #ATM端管理员账户以及密码
