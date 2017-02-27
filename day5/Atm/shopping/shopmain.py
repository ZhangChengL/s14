#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
import sys
import json
import time
from core import auth
from conf import set
from core import logger
from core import userinfo
from core import transactions
from core import main

shop_user={
    'user_id':None,
    'by_id':None,
    'shop_by':None
}

good_by = []

def shop_login():
    '''
    商场登录接口
    :return:
    '''
    user_date=auth.shop_login(shop_user)
    if user_date:
        shop_index(user_date)


def shop_register():
    '''
    商场注册接口
    :return:
    '''
    user_add_id = input('请输入注册ID>>>:')
    user_add_ps = input('请输入注册密码>>>:')
    user_atm_id = input('请输入需要绑定的银行卡ID>>>:')
    user_atm_pw = input('请输入需要绑定的银行卡密码>>>:')
    userinfo.shop_dump_info(user_add_id,user_add_ps,user_atm_id,user_atm_pw)

def login_out():
    exit()

def shopping(user_date):
    '''
    购物接口
    :param user_date:
    :return:
    '''
    good=open(set.BD_GOODS,'r',encoding='utf-8').read()
    goods=eval(good)
    for index, item in enumerate(goods):
        print(index, item)
    while True:
        good_id = input('输入你需要购买的商品ID，按e键可结束购买:')
        if good_id.isdigit():
            good_id = int(good_id)
            if good_id < len(goods) and good_id >= 0:
                good_by.append(goods[good_id])
                print('\033[1;34m你选择的商品%s已加入购物车\033[0m' % goods[good_id])
            else:
                print('你输入的商品序号不存在！')
        elif good_id == 'e':
            user_date['shop_by']=good_by
            break
        else:
            print('输入错误！')



def shopping_cart(user_date):
    '''
    查看与结算购物车接口
    :param user_date:
    :return:
    '''
    user_shop=user_date[ 'shop_by']
    if user_shop == None:
        print('购物车为空！')
    else:
        by_Ture=True
        while by_Ture:
            print('你本次购物车内容为：')
            for index, item in enumerate(user_shop):
                print(index, item)
            cart_choise=input('按商品对应序号可进行删除商品，按w键可进行结算，按e键继续购物:')
            if cart_choise.isdigit():
                cart_choises=int(cart_choise)
                if cart_choises < len(user_shop) and cart_choises >= 0:
                    del user_shop[cart_choises]
                    user_date['shop_by'] = user_shop
                    print('该商品已删除！')
            elif cart_choise == 'e':
                break
            elif cart_choise == 'w':
                good_price=0
                for i in user_shop:
                    good_price = good_price + int(i[1])
                ps_time=0
                while ps_time <3:
                    atm_date=userinfo.load_info(user_date['by_id'])
                    atm_pswd=input('请输入银行卡密码>>>:')
                    if atm_date['password']==atm_pswd:
                        new_money = transactions.money_change(atm_date, 'consume', good_price, main.trans_logger)
                        print('本次购物总共消费：%s,剩余银行卡余额：%s' %(good_price,new_money['money']))
                        shop_re=userinfo.re_load_info(user_date['user_id'])
                        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        shop_re[now_time]=user_shop
                        userinfo.re_dump_info(user_date['user_id'],shop_re)
                        good_by.clear()
                        user_date['shop_by']=None
                        by_Ture=False
                        break
                    else:
                        print('输入密码错误，请核对后重新输入！')
                        ps_time =ps_time+1
                else:
                    print('连续输入错误3次，强制退出！')
                    break



            else:
                print('输入错误！')


def shop_log(user_date):
    '''
    消费记录接口
    :param user_date:
    :return:
    '''
    shop_re = userinfo.re_load_info(user_date['user_id'])
    for i in shop_re:
        print(i,shop_re[i])




def index_out(user_date):
    exit()


def shop_index(user_date):
    index ='''
    \033[1;32m
    ================Welcome================
        1.购物
        2.查看购物车与结算
        3.查询消费记录
        4.退出\033[0m
    '''
    index_dict={
        '1':shopping,
        '2':shopping_cart,
        '3':shop_log,
        '4':index_out,
    }
    while True:
        print(index)
        index_choise=input('请选择>>>:').strip()
        if index_choise in index_dict:
            index_dict[index_choise](user_date)



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
        choise=input('请选择>>>:').strip()
        if choise in menu_dict:
            menu_dict[choise]()
        else:
            print('输入错误！')
