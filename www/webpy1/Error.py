#-*- encoding:utf-8 -*-

# 错误相关的函数

import json

def errResult(code,reason):
    return json.dumps({'code':code,'reason':reason})