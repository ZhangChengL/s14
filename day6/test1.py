#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import  re
content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new_content = re.split('\*', content)
# new_content = re.split('\*', content, 1)
print(new_content)
content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new_content = re.split('[\+\-\*\/]+', content)
# new_content = re.split('\*', content, 1)
print(new_content)
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group())
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups())