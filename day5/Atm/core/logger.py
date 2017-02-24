#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import  logging
import os
from conf import set
def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    pout = logging.StreamHandler()
    pout.setLevel(logging.INFO)

    log_file='%s/log/%s'%(set.BASE_DIR,set.LOG_TYPE[log_type])
    fin = logging.FileHandler(log_file)
    fin.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    pout.setFormatter(formatter)
    fin.setFormatter(formatter)

    logger.addHandler(pout)
    logger.addHandler(fin)

    return logger