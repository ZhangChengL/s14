#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl

menu = {
    '四川':{
        '成都':{
            '成华区':{
                '电子科技大学':{},
                '成都动物园':{},

            },
            '武侯区':{
                '玉林':{},
                '神仙树':{},

            },
            '高新区':{
                '高新国际广场':{},
            },
        },
        '绵阳':{
            '江油':{
                '老男孩':{},
                '北航':{},
            },
            '三台':{}

        },
  },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{
            '机场':{
                'T2航站楼':{}
            }
        },
    },
   }
#m1 = open('menu','r',encoding='utf-8')

while True:
    for i in menu:
        print(i)
    chooes = input(">>>请选择1，按e退出：")
    if chooes in menu:
            while True:
                for i2 in menu[chooes]:
                    print(i2)
                chooes2 = input(">>>请选择2，按b返回，按e退出：")
                if chooes2 in menu[chooes]:
                    while True:
                        for i3 in menu[chooes][chooes2]:
                            print(i3)
                        chooes3 = input(">>>请选择3，按b返回，按e退出：")
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

    #elif chooes == 'b':
     #   break
    elif chooes2 == 'e':
        exit()
    else:
        pass