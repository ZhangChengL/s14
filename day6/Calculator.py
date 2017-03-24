#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# 模拟计算器开发：
#
# 实现加减乘除及拓号优先级解析
#
# 用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
# 运算后得出结果，结果必须与真实的计算器所得出的结果一致

# hint:
#
# re.search(r'\([^()]+\)',s).group()
#
# '(-40/5)'
# import re
# s = '(-60-30+10-22) +(-40/-5)'
# a=re.search(r'\([^()]+\)',s).group()
# print(a)
# b=a.split('(')[1].split(')')[0]
# print(b)
# sz=re.split('[-+]',b) #筛选加减
# fh=re.findall('[-+]',b) #筛选数值
# #re.search('[*/]')
# print(fh)
# print(sz)
# print(len(b))
import re

def compute(formula):
    #formulas=formula.split('(')[1].split(')')[0]
    formulas=formula.strip('()')
    print(formulas)
    sz=re.split('[-+]',formulas)
    print(sz)
    fh=re.findall('[-+]',formulas)
    print(fh)
    if len(sz[0].strip())==0:
        sz[1]=fh[0]+sz[1]
        del sz[0]
        del fh[0]
        print(sz)
        print(fh)
    for index,i in enumerate(sz):
        i = i.strip()
        if i.endswith('*') or i.endswith('/'):

    return formulas
def calc(formula):
    brackets_is=True
    while brackets_is:
        bk=re.search(r'\([^()]+\)',formula)
        if bk:
            formula=formula.replace(bk.group(),str(compute(bk.group())))
        else:
            compute(formula)
            brackets_is=False

cc=calc('(-60-30+10-22) +(-40/-5)')