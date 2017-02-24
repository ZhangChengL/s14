#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from core import main
from shopping import shopmain

def atm():
    atm_menu='''
    ---------Welcome----------
    1. 普通用户登录
    2. 管理员登录
    '''
    while True:
        print(atm_menu)
        login_choise=input('请选择>>>>')
        if login_choise == '1':
            main.userrun()
        elif login_choise == '2':
            main.adminrun()
        else:
            print('输入错误！')

index_menu='''
---------Welcome----------
1.ATM
2.商店
'''
while True:
    print(index_menu)
    index_choise=input('请选择>>>:')
    if index_choise == '1':
        atm()
    if index_choise == '2':
        shopmain.shop_mian()


