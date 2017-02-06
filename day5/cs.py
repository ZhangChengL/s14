#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Zhangcl
# import hashlib
# hash = hashlib.md5(b'898oaFs09f')
# hash.update(b'admin')
# print(hash.hexdigest())
import hmac
h = hmac.new(b'wueiqi')
h.update(b'hellowo')
print(h.hexdigest())