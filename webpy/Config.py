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

SESSION_EXPIRETIME = 3000
LOGIN_INVALID_TIME = 3000


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

KEY_LOGINE = "KEY_LOGINE_{userid}"

KEY_SHOP_CFG_INVENTORY = "KEY_SHOP_CFG_INVENTORY_{pid}"

# 任务的key
KEY_TASK = "KEY_TASK_{userid}_{date}"