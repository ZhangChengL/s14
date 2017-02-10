#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import re
a='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(re.search(r'\([^()]+\)',a).group())

# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('\*', content)
# # new_content = re.split('\*', content, 1)
# print (new_content)
#
#
# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('[\+\-\*\/]+', content)
# # new_content = re.split('\*', content, 1)
# print (new_content)
#
# inpp = '1-2*((60-30 +(-40-5)*(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
# inpp = re.sub('\s*','',inpp)
# new_content = re.split('\(([\+\-\*\/]?\d+[\+\-\*\/]?\d+){1}\)', inpp, 1)
# print (new_content)

a='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
print(re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', a).group())
bf,af=re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', a, 1)
print(bf)
print(af)
print(eval(a))