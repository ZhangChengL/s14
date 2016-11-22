#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


while True:
    for i in menu:
        print(i)
    chooes = input(">>>请选择1：")
    if chooes in menu:
            while True:
                for i2 in menu[chooes]:
                    print(i2)
                chooes2 = input(">>>请选择2：")
                if chooes2 in menu[chooes]:
                    while True:
                        for i3 in menu[chooes][chooes2]:
                            print(i3)
                        chooes3 = input(">>>请选择3：")
                        if chooes3 in menu[chooes][chooes2]:
                            #while True:
                                for i4 in menu[chooes][chooes2][chooes3]:
                                    print(i4)
                                chooes4 = input('最后一层，按b返回，按e退出：')
                                if chooes4 == 'b':
                                    break
                                elif chooes4 == 'e':
                                    exit()
                                else:
                                    pass
                        elif chooes3 =='b':
                            break
                        elif chooes3 == 'e':
                            exit()
                        else:
                            pass

                elif chooes2 =='b':
                     break
                elif chooes2 == 'e':
                    exit()
                else:
                    pass

    elif chooes == 'b':
        break
    elif chooes2 == 'e':
        exit()
    else:
        pass