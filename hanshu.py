#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
#def stu_register(name,age,country,course):
def stu_register(name,age,course,country="CN"): #使用关键参数设置默认值，关键参数必须放在位置参数之后。
    print("----注册学生信息------")
    print("姓名:",name)
    print("age:",age)
    print("国籍:",country)
    print("课程:",course)

stu_register("王山炮",22,"CN","python_devops")
stu_register("刘老根",25,"CN","linux")
stu_register('傻逼',22,'linux')

name = "Alex"


def change_name():
    name = "Alex2"

    def change_name2():
        name = "Alex3"
        print("第3层打印", name)

    change_name2()  # 调用内层函数
    print("第2层打印", name)


change_name()
print("最外层打印", name)


def calc(n):
    print(n)
    if int(n / 2) == 0:
        return n
    return calc(int(n / 2))


calc(10)

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]


def binary_search(dataset, find_num):
    print(dataset)

    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:  # find it
            print("找到数字", dataset[mid])
        elif dataset[mid] > find_num:  # 找的数在mid左面
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:  # 找的数在mid右面
            print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:  # find it
            print("找到数字啦", dataset[0])
        else:
            print("没的分了,要找的数字[%s]不在列表里" % find_num)


binary_search(data, 66)

res = map(lambda x:x**2,[1,5,7,4,8])
for i in res:
    print(i)

name1 ='zcl'
sc = 'old boy'
def change_name(name1):
    global sc
    sc = 'MG'
    print('before change:',name1,sc)
    name1 = 'ZCL'
    print('after name:',name1,sc)
change_name(name1)
print('全局：',name1,sc)

