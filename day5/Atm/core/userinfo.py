#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import json
import os
import time
import datetime
from conf import set
def dump_info(acc_date):
    user_path=set.DATABASE
    user_file ='%s/%s.json' %(user_path,acc_date['id'])
    with open(user_file,'w') as f:
        userdate = json.dump(acc_date,f)
    return True

def re_dump_info(user_id,acc_date):
    user_path=set.SHOP_RE_DATABASE
    user_file ='%s/%s_re.json' %(user_path,user_id)
    with open(user_file,'w') as f:
        userdate = json.dump(acc_date,f)
    return True

def load_info(acc_date):
    user_path=set.DATABASE
    user_file = '%s/%s.json' % (user_path, acc_date)
    if os.path.isfile(user_file):
        with open(user_file) as f:
            acc_data = json.load(f)
            return  acc_data


def re_load_info(acc_date):
    user_path=set.SHOP_RE_DATABASE
    user_file = '%s/%s_re.json' % (user_path, acc_date)
    if os.path.isfile(user_file):
        with open(user_file) as f:
            acc_data = json.load(f)
            return  acc_data


def admin_dump_info(user_add_id,admin_logger):
    user_path = set.DATABASE
    user_file = '%s/%s.json'%(user_path,user_add_id)
    if os.path.isfile(user_file) is not True:
        now_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        ft_time=datetime.date.today() + datetime.timedelta(days=1825)
        ft_times=ft_time.strftime('%Y-%m-%d')
        acc_dic={
            'id':user_add_id,
            'password':'abc',
            'credit': 15000,
            'money':15000,
            'enroll_date':now_time,
            'expire_date':ft_times,
            'status':0
        }
        with open(user_file,'w') as f:
            userdate= json.dump(acc_dic,f)
        admin_logger.info('user:%s Create success!')
        return True
    else:
        print('用户ID重复，请确认后重新创建！')

def shop_dump_info(sp_user_id,sp_user_ps,user_atm_id,user_atm_pw):
    user_path = set.SHOP_DATABASE
    atm_path=set.DATABASE
    shop_re_path=set.SHOP_RE_DATABASE
    user_file='%s/%s.json'%(user_path,sp_user_id)
    atm_file='%s/%s.json'%(atm_path,user_atm_id)
    shop_re_file='%s/%s_re.json' %(shop_re_path,sp_user_id)
    if os.path.isfile(user_file) is not True:
        if os.path.isfile(atm_file):
            with open(atm_file) as f:
                atm_data = json.load(f)
                if atm_data['password']==user_atm_pw:
                    acc_dic={
                        'id':sp_user_id,
                        'password':sp_user_ps,
                        'atmID':user_atm_id
                    }
                    with open(user_file,'w') as f:
                        user_date = json.dump(acc_dic,f)
                    re_dic={}
                    with open(shop_re_file,'w') as f_re:
                        re_date = json.dump(re_dic,f_re)
                    print('创建成功！')
                    return True
                else:
                    print('银行卡密码错误！')
        else:
            print('未查询到该银行卡号码！')
    else:
        print('用户ID重复，请确认后重新创建！')