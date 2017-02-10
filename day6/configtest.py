#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
import configparser
config=configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
   config.write(configfile)

config=configparser.ConfigParser()
config.read('example.ini')#将配置文件读进来
print(config.sections())#打印全部，默认不打印[DEFAULT]中的内容
print('zzz' in config)#判读是否在配置文件内
print(config['bitbucket.org']['user'])
topsecret = config['topsecret.server.com']
print(topsecret['host port'])
for key,val in config['bitbucket.org'].items(): #打印默认[DEFAULT]和指定的内容
    print(key,val)

for key in config['bitbucket.org']: #打印默认[DEFAULT]和指定的内容
    print(key)

print(config.options('topsecret.server.com'))#打印对应配置内容
print(config.items('topsecret.server.com'))#打印对应配置内容包含值
config.remove_section('bitbucket.org') #删除对应配置选项
config.write(open('configtest.ini','w'))
if config.has_section('zcl')==False:#判读是否存在
    config.add_section('zcl')#添加配置选项
    config.write(open('example.ini', 'w'))
config.set('zcl','host port','123456')#创建配置内容
config.write(open('example.ini','w'))
config.add_section('bitbucket.org')
config.write(open('example.ini','w'))
config.set('bitbucket.org','user','yes')
config.write(open('example.ini','w'))
config.set('zcl','kkk','123456')#创建配置内容
config.write(open('example.ini','w'))
config.remove_option('zcl','kkk')#删除指定配置选项内的指定内容
config.write(open('example.ini','w'))