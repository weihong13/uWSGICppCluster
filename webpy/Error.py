#-*- encoding:utf-8 -*-

# 错误相关的函数

import json

def ErrResult(code,reason):
    return json.dumps({'code':code,'reason':reason})