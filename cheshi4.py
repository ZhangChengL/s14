#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# for accmoney in acc_mon:
#     login_user, login_money = accmoney.strip().split()
#     loginuser = False
#     if yourname == login_user:
#
#         loginuser = True
#         print(loginuser)
#         print('尊敬的客户你好，你所剩余额为：\033[1;31m%s\033[0m' % login_money)
#         print(loginuser)
#         break
#     elif yourname != login_user:
#         break
#         # if loginuser == False:
#         #     yourmoney=input('第一次登录，请输入购物金额:')
#         #     user_money_add ='\n' + yourname +' '+ yourmoney
#         #     acc_mon.write(user_money_add)
#         #     print('金额录入成功，你所剩余额为：\033[1;31m%s\033[0m' %yourmoney)
#         # elif loginuser == True:
#         #     print('传递成功')
#     print(loginuser)
# def input_backend():
#     yourserver = input('input server:')
#     yourweight = input('input weight:')
#     yourmaxconn = input('input maxconn:')
#     your_new_server = 'server' + ' ' + yourserver + ' ' + 'weight' + ' ' + yourweight + ' ' + 'maxconn' + ' ' + yourmaxconn
#     return your_new_server,yourserver,yourweight,yourmaxconn
#
# x = input_backend(yourserver)
# print(x)

#
# dell='_'
# cc=['alex', 'eric', 'rain']
# aa=dell.join(cc)
# print(aa)
i = 2
a = 0
while i <101:
    if i % 2 == 0:
        a=a+i
    else:
        a=a-i
    i=i+1
print(a)
