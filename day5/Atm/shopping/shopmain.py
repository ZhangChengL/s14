#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
import json
from core import auth
from conf import set
from core import logger
from core import userinfo
from core import transactions


def shop_login():
    pass


def shop_register():
    user_add_id = input('请输入注册ID>>>:')
    user_add_ps = input('请输入注册密码>>>:')
    user_atm_id = input('请输入需要绑定的银行卡ID>>>:')
    userinfo.shop_dump_info(user_add_id,user_add_ps,user_atm_id)

def login_out():
    exit()




def shop_mian():
    menu ='''
    \033[1;32m
    1.登录
    2.注册
    3.退出\033[0m
    '''
    menu_dict={
        '1':shop_login,
        '2':shop_register,
        '3':login_out,
    }
    while True:
        print(menu)
        choise=input('请选择>>>:')
        if choise in menu_dict:
            menu_dict[choise]()
        else:
            print('输入错误！')
