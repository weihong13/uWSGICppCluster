#-*- encoding:utf-8 -*-

import web

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

DEFAULT_SECPASSWORD = '123456'
USER_STATUS_NOLMAL = 0
USER_STATUS_FRERZE = 1