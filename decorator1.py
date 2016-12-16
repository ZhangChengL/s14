#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
user = 'zzz'
passwd = '123456'
def login(auth_type):
    def auth(func):
        def deco(*args,**kwargs):
            if auth_type == 'qq':
                username = input('username:')
                password = input('password:')
                if user == username and passwd ==password:
                    print('the auth is success!')
                    func(*args,**kwargs)
                else:
                    exit('the auth is faild')
            elif auth_type == 'wechat':
                print('不会写！')
        return deco
    return auth
def index():
    print('welcome to index')
@login(auth_type='qq')
def home(page):
    print('welcome to home')
@login(auth_type='wechat') #bbs() = auth(bbs)()
def bbs():
    print('welcome to bbs')

index()
home(1)
bbs()
