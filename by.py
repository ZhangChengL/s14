#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
good = [['1','iphone7',6888],
        ['2','辣条',10],
        ['3','小浣熊干脆面',5],
        ['4','小米4',1500]]
good_by = []
#balance = 0
print(good)
money=int(input('输入的你金额：'))
while True:
    good_id = input('输入你需要购买的商品ID:')
    if good_id == 'q':
        print("your chooes:", good_by)
        print('余额：', money)
        break
    elif int(good_id) < len(good)+1 and int(good_id)>0:
        good_by.append(good[int(good_id) - 1])
        if int(good_by[-1][2]) > money:
            print("穷鬼你没辣么多钱！")
            good_by.pop()
            #continue
        else:

            money = money - int(good_by[-1][2])
            #continue
    else:
        print("输入错误")
        #continue
