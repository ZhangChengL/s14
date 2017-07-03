#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_INFO_PATH = os.path.join(BASE_DIR,'db')
USER_FILE_PATH = os.path.join(BASE_DIR,'file_data')
ADMIN_INFO = {
    'username':'admin',
    'password':'123456'
}
Default_password = '123456'