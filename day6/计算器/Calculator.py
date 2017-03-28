#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# 模拟计算器开发：
# 实现加减乘除及拓号优先级解析
# 用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
# 运算后得出结果，结果必须与真实的计算器所得出的结果一致
import re
# hint:
# re.search(r'\([^()]+\)',s).group()
# '(-40/5)'
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


def remove_symbol(formula): #判断有两个连续加减运算符出现的情况
    formula = formula.replace("++", "+")
    formula = formula.replace("+-", "-")
    formula = formula.replace("-+", "-")
    formula = formula.replace("--", "+")
    formula = formula.replace("- -", "+")
    return formula

def compute_mutiply_and_dividend(formula):   #这里是计算乘除法
    operators = re.findall("[*/]", formula) #取出运算符
    calc_list = re.split("[*/]", formula) #取出数值
    res = None #存放计算结果
    for index, i in enumerate(calc_list):
        if res:
            if operators[index - 1] == "*":
                res *= float(i)
            elif operators[index - 1] == "/":
                res /= float(i)
        else:
            res = float(i)

    print("\033[31;1m[%s]运算结果=\033[0m" % formula, res)
    return res


def compute(formula):
    #formulas=formula.split('(')[1].split(')')[0]
    formulas=formula.strip('()') #剥掉括号
    formulas=remove_symbol(formulas) #将连续的运算符替换掉
    print('\033[31;1m筛选括号内容：%s\033[0m' %formulas)
    sz=re.split('[-+]',formulas) #筛选出数字
    print(sz)
    fh=re.findall('[-+]',formulas) #筛选出运算符
    print(fh)
    if len(sz[0].strip())==0: #如果筛选出的数字列表第一个值是空，那就说明第一个数字是负数
        sz[1]=fh[0]+sz[1] #修改对应数值
        del sz[0]
        del fh[0]
        print(sz)
        print(fh)
    for index,x in enumerate(sz): #判断出现乘除运算符之后的数据会是负数的情况，如果是负数会将数值隔开，数值列表会出现一个空数值
        x=x.strip()
        if x.endswith("*") or x.endswith("/"):
            sz[index]=sz[index]+fh[index]+sz[index+1] #将负数值直接手动写到前一个乘除运算符后面
            del sz[index+1]
            del fh[index]
    for index,i in enumerate(sz): #这里计算乘除法
        if re.search("[*/]", i):
            sub_res = compute_mutiply_and_dividend(i)
            sz[index] = sub_res
    print(sz, fh)
    #这里开始算加减
    total_res = None #设置一个变量存放计算后数值
    for index, item in enumerate(sz):
        if total_res:  # 代表不是第一次循环
            if fh[index - 1] == '+':
                total_res += float(item)
            elif fh[index - 1] == '-':
                total_res -= float(item)
        else: #第一次计算，首个数值存入
            total_res = float(item)
    print("\033[32;1m[%s]运算结果:\033[0m" % formula, total_res)
    return total_res



def calc(formula):
    brackets_is=True
    while brackets_is:
        bk=re.search(r'\([^()]+\)',formula)  #判断字符串内是否有括号
        if bk: #先计算括号内容
            # formula=formula.replace(bk.group(),str(compute(bk.group())))
            results = compute(bk.group()) #取出括号内容
            formula = formula.replace(bk.group(), str(results)) #将计算结果替换原括号内容

        else:  #没有括号内容啦
            print('\n\033[42;1m计算出的最终结果:\033[0m', compute(formula))
            #compute(formula)
            brackets_is=False

#cc=calc('(-60-30+10-22) +(-40/-5)')
#res = calc("1 - 2 * ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )")
user_input=input('输入需要计算的字符串：')
#res = calc('33 * (1+5-7/-8*10-12+10+(10-3/2+10*2))/(10-2/2-1*3+(2-3+2*9/3))')
res=calc(user_input)
print('\033[42;1meval验证的最终结果:\033[0m',eval(user_input))