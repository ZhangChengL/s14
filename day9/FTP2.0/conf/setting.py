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

Ps = '''\033[1;32m
        ============================================================
        Ps:
        上传文件格式：put x:/xxx/xxx（文件完整路径）
        下载文件格式：get xxx(文件名)  x:/xxx/xxx/ (需要存放的本地目录)
        查看目录下文件：ls
        ============================================================
        \033[0m'''