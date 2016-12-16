#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#
# def decorartor(func):
#     def wrapper(n):
#         print('starting')
#         func(n)
#         print('stopping')
#
#     return wrapper
#
#
# def test(n):
#     print('in the test arg is %s' % n)

#
# decorartor(test)('alex')

def decorartor(func):
    def wrapper(*args, **kwargs):
        print('starting')
        func(*args, **kwargs)
        print('stopping')

    return wrapper
def test(n, x=1):
    print('in the test arg is %s' %n,x)
decorartor(test)('alex', x=2)

# import time
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print('run time is %s ' % (stop - start))
#         print('timeout')
#
#     return wrapper
#
#
# @decorator
# def test(list_test):
#     for i in list_test:
#         time.sleep(0.1)
#         print('-' * 20, i)
#
#
# # decorator(test)(range(10))
# test(range(10))
# import time
#
#
# def timer(timeout=0):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             func(*args, **kwargs)
#             stop = time.time()
#             print('run time is %s ' % (stop - start))
#             print('timeout')
#
#         return wrapper
#
#     return decorator
#
#
# @timer(10)
# def test(list_test):
#     for i in list_test:
#         time.sleep(0.1)
#         print('-' * 20, i)
#
#
# # timer(timeout=10)(test)(range(10))
# test(range(10))
#
# def bar():
#     print ('in the bar')
# def foo(func):
#     res=func()
#     return res
# foo(bar)
#
#
# def foo(func):
#     return func
#
#
# print('Function body is %s' % (foo(bar)))
# print('Function name is %s' % (foo(bar).func_name))
# foo(bar)()
# # foo(bar)() 等同于bar=foo(bar)然后bar()
# bar = foo(bar)
# bar()