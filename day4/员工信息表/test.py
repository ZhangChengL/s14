# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author:Zhangcl
# #_*_coding:utf-8_*_
# import os
# def fetch(data):
#     #查询语法一：select name,age from staff_table where age > 22
#     #查询语法二：select * from staff_table where dept = IT
#     data1 = data.split(" ")
#     directory = ["staff_id", "name", "age", "phone", "dept", "enroll-date"]
#     if data == ("select name,age from staff_table where age > %s" %(data1[7])):
#                 with open("staff_table.txt", encoding="utf-8") as f:
#                     list = []
#                     list1 = []
#                     list2 = []
#                     for line in f:
#                         i = line.strip().split(",")
#                         w = i[1]
#                         e = i[2]
#                         a = [w, e]
#                         if e > data1[7]:
#                             list2.append(a)
#                     for i in list2:
#                         print(i)
#                     print("查询到 %s 条符合的信息" %len(list2))
#     else:
#          with open("xinxi", encoding="utf-8") as f:
#              list = []
#              for line in f:
#                  i = line.strip().split(",")
#                  q = i[0]
#                  w = i[1]
#                  e = i[2]
#                  r = i[3]
#                  t = i[4]
#                  y = i[5]
#                  if data == ("select * from staff_table where %s = %s" % (data1[5], i[(directory.index(data1[5]))])):
#                          list.append(i)
#                  else:
#                      continue
#              for j in list:
#                   print('.'.join(j))
#              print("查询到 %s 条符合的信息" %len(list))
#              return 0
# def add(data):
#     #添加语法： name,age,phone,dept,enroll-date  (例如：孙凯,22,11111111111,IT,2016-12-12)
#     data1 = data.split(",")
#     f=  open("xinxi",encoding="utf-8")
#     all_list = []
#     list = []
#     phone_list = []
#     for line in f:
#             i = line.strip().split(",")
#             q = i[3]
#             phone_list.append(q)
#
#     if data1[2] in phone_list:
#                 print("手机号已存在")
#                 f.close()
#     else:
#                 f1 = open("xinxi", "r+", encoding="utf-8")
#                 for line in f1:
#                         lines = line.strip().split(",")
#                         # print(lines)
#                         list.append(lines)
#                         i = line.strip().split(",")
#                 w = str(int(list[-1][0]) + 1)
#                 data1.insert(0, w)
#                 print(data1)
#                 data1 = ','.join(data1)
#                 f1.write("\n")
#                 f1.write(data1)
#                 f1.close()
#                 print("添加成功!!!")
# def remove(data):
#     #删除语法：delete from staff_table where staff_id = 12
#    data1 = data.split(" ")
#    if data == ("delete from staff_table where staff_id = %s" %data1[6]):
#        with open("xinxi", encoding="utf-8") as f:
#            list = []
#            for line in f:
#                i = line.strip().split(",")
#                i1 = line.splitlines()
#                q = i[0]
#                if data1[6] == q:
#                    i2 = ','.join(i1)
#                    print(i2)
#                    list.append(i)
#        a = i2
#        f = open("xinxi", encoding="utf-8")
#        f1 = open("back", "a+", encoding="utf-8")
#        for i in f:
#            if a in i:
#                i = i.replace(a, "").strip()
#            f1.write(i)
#            f1.flush()
#        f.close()
#        f1.close()
#    os.remove("xinxi")
#    os.rename("back","xinxi")
#    print("删除成功！！！")
#    return
# def change(data):
#     #修改请输入（注意空格和没有引号）：UPDATE staff_table SET dept = IT where dept = 运维
#     data1 = data.split(" ")
#     print(data1)
#     # a =','.join(data1[3])
#     # print(a)
#     directory = ["staff_id", "name", "age", "phone", "dept", "enroll-date"]
#     var = int(directory.index(data1[3]))
#     with open("xinxi", encoding="utf-8") as f,\
#           open("back","w",encoding="utf-8")as f1:
#         for line in f:
#             lines = line.strip()
#             print(lines)
#             if  data1[5] in lines:
#                 lines = lines.replace(data1[5],data1[9])
#             f1.write(lines)
#             f1.write("\n")
#             f1.flush()
#     os.remove("xinxi")
#     os.rename("back","xinxi")
#     print("修改成功!!!")
#
# if __name__ == "__main__":
#     msg = """
#     1:查询
#     2:添加
#     3:删除
#     4:修改
#     5:退出
#     """
#     msg_dict = {
#         "1": fetch,
#         "2": add,
#         "3": remove,
#         "4": change,
#         "5": exit,
#     }
#     while True:
#         print(msg)
#         choice = input("输入序号>>:")
#         if len(choice) == 0 or choice not in msg_dict: continue
#         if choice =='5':break
#         data = input("请输入数据>>:").strip()
#         msg_dict[choice](data)
import re
# aa='insert into emp values(狗蛋,24,15882060129,it,2017-01-23)'
# sql_list=re.split(' ',aa)
# print(aa)
# cc=re.search('\(.*\)',aa).group()
# ccc=cc.split('(')[1].split(')')[0].split(',')
# print(' '.join(ccc))
# aaaaa=['6', '狗蛋', '24', '1237889712', 'it', '2017-01-23']
# aab=' '.join(aaaaa)
# print(aab)
#
# chag = {
#     'staff_id': 0,
#     'name': 1,
#     'age': 2,
#     'phone': 3,
#     'dept': 4,
#     'enroll_date': 5
# }
#
# print(chag['age'])
# a=['aa','bbb','cc','ff']
# cc=['name','age']
# for i in cc:
#     print(a[chag[i]])
# import re
# sql=input('sql>>')
# if re.search("^(?i)select",sql) is not None:
#     print('yes')
# else:
#     print('no')

import time
import datetime
now_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
f_time=datetime.date.today() + datetime.timedelta(days=1825)
print(now_time)
print(f_time)


import datetime
print (datetime.datetime.now())
cc_time=datetime.datetime.now() - datetime.timedelta(days=5)
print(cc_time.strftime('%Y-%m-%d'))