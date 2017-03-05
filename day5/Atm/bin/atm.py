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
    atm_menu='''\033[1;31m
    ---------Welcome----------
    1. 普通用户登录
    2. 管理员登录
    3. 退出\033[0m
    '''
    while True:
        print(atm_menu)
        login_choise=input('请选择>>>>')
        if login_choise == '1':
            main.userrun()
        elif login_choise == '2':
            main.adminrun()
        elif login_choise == '3':
            exit()
        else:
            print('\033[1;31m输入错误！！\033[0m')

index_menu='''\033[1;34m
---------Welcome----------
1.ATM
2.商店\033[0m
'''
while True:
    print(index_menu)
    index_choise=input('请选择>>>:')
    if index_choise == '1':
        atm()
    if index_choise == '2':
        shopmain.shop_mian()


