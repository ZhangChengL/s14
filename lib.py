# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author:Zhangcl
# name = [['zzz','123'],['ccc','123']]
# hmd=[]
# con=0
#
# for i in range(na):
#     #print(i[0])
#     yourname = input('输入用户名：')
#     password = input('输入密码：')
#     if yourname == i[0] and password == i[1]:
#         print('登录成功')
#         exit()
#     if yourname == i[0] and password!=i[1]:
#         print('密码错误，请重新输入')
#         con = con +1
#         if con ==3:
#             hmd.append(yourname)
#             print(hmd)
#
#         break
#     if yourname in hmd:
#         print('已连续输错3次，账户已锁定')
#         exit()
#     if yourname != i[0]:
#         print('账户不存在，请确认账户是否正确')
#         exit()

acc = open('acc','r',encoding='utf-8')
black = open('black','r+',encoding='utf-8')
con =0
yourname = input('请输入用户名：')
while True:
    for black_line in black:
        black_line = black_line.strip()
        if yourname == black_line:
            print('用户已锁定，退出')
            exit()
    acc_line = acc.readline()
    for acc_list in acc_line:
        password = input('请输入密码：')
        (user,pawd) = acc_line.strip().split()
        if user == yourname and pawd == password:
            print('输入正确，登录成功！')
            exit()
        else:
            print('密码错误，请重新输入！')
            con = con +1
            break
    if con ==3:
        black.write(yourname)
        print('连续输错3次，账户已锁定')
        exit()
acc.close()
black.close()