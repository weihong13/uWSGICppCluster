#-*- encoding:utf-8 -*-

import web
import redis # type: ignore

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'weihong'
DB_PW = '171223'
DB_NAME = 'webpy'

gdb = web.database(
    dbn = 'mysql',
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    pw = DB_PW,
    db = DB_NAME 
)

RDS_HOST = '127.0.0.1' 
RDS_PORT = 6379
RDS_PW = '171223'

SESSION_EXPIRETIME = 30


grds = redis.Redis(
    host=RDS_HOST,
    port=RDS_PORT,
    password=RDS_PW
)

DEFAULT_SECPASSWORD = '123456'
NEWUSER_DEFAULT_COIN = 10000

USER_STATUS_NOLMAL = 0
USER_STATUS_FRERZE = 1


# 账号
KEY_PACKAGE = "KEY_PACKAGE_{userid}"