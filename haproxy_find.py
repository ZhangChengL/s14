#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import json

def haproxy_find(arg):
    bg = False
    cx = []
    with open('haproxy','r',encoding='utf-8') as f:
        for i in f:
            if i.strip() == "backend %s" %arg:
                #print(i)
                bg=True
                continue
            if i.strip().startswith('backend'):
                bg = False
            if bg == True:
                cx.append(i)
    return cx
backend = input('input your backend:')
x = haproxy_find('%s' %backend)
print(backend)
for i in x:
    print(i)


# haproxy_find('www.oldboy.org')

# with open('haproxy','r',encoding='utf-8') as f:
#     for i in f:
#         if i.strip() == 'backend www.oldboy.org':
#             print(i)


# def select(arg):
#     """
#     要求用户输入域名，可以查看webserver的子作用域
#     针对haproxy的配置文件
#     思路：
#     a.逐行读取文件
#     b.当我遇到backend + 域名的行的时候，将其子作用域放到一个空列表显示给用户看
#     c.再当我遇到以backend开头的时候就结束循环就ok了
#     d.因为这个子作用域是需要显示 的，就要拿出来，所以要特别显示出来，要与众不同，所以我们在这里定义标志位来显示这个与众不同
#     :param arg:
#     :return:
#     """
#     result = []
#     flag = False
#     with open("haproxy", "r", encoding="utf-8") as f:
#         for line in f :
#             if line.strip() == "backend %s" % arg:
#                 flag = True
#                 continue
#             if line.strip().startswith("backend"):
#                 flag  = False
#             if flag:
#                 result.append(line)
#     return result
# ret = select("www.oldboy.org")
#
# for i in ret :
#     print(i)