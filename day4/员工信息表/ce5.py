#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
f=open('staff_table.txt','r',encoding='utf-8')
staff_table="staff_table.txt"
staff_old =open(staff_table,'r',encoding='utf-8')
# for i in f:
#     a=i.split(' ')
#     if a[-2]=='IT':
#         print(a)
# for i in f:
#     print(i)
#     if i.strip()=='':
#         print('yes')
#     else:
#         print('No')
# for i in staff_old:
#     print(i
fff=staff_old.read()
print(len(fff))
  #  print('yes')

# for i in xx:
#     for cc in bb:


while True:
    print(meg_up_find)
    up_user_choise = input('请选择：')
    if up_user_choise.isdigit():
        up_user_choises = int(up_user_choise)
        you_want_to_up = input('请输入需要被修改的内容：')
        print(meg_to_up)
        up_to_choise = input('请选择：')
        you_new_to_up = input('请输入修改后的内容：')
        if up_user_choises in (1, 2, 3, 4, 5):
            for i in staff_old:
                a = i.split(' ')
                if a[up_user_choises - 1] == you_want_to_up:
                    # cc = ' '.join(a)
                    print(a)
        else:
            print('输入错误')
    else:
        print('输入错误')