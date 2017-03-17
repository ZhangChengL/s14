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