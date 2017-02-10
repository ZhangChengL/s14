#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import logging
import time
from logging import handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler(filename='timelog.log',when='S',interval=2,backupCount=4)
fh.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(filename)s   %(levelname)s : %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
logger.info('this is info')
logger.warning('this is warning')
time.sleep(2)
logger.error('this is error')
logger.info('this is info2')
time.sleep(2)
logger.warning('this is warning2')