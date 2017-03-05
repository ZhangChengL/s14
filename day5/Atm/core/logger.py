#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import  logging
import os
from conf import set
def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    pout = logging.StreamHandler() #打印在屏幕
    pout.setLevel(logging.INFO)

    log_file='%s/log/%s'%(set.BASE_DIR,set.LOG_TYPE[log_type])
    fin = logging.FileHandler(log_file) #打印在文件内
    fin.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #设置日志格式

    pout.setFormatter(formatter)
    fin.setFormatter(formatter)

    logger.addHandler(pout)
    logger.addHandler(fin)

    return logger