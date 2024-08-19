#-*- encoding:utf-8 -*-

import Config

# 操作数据库的模块

# 插入一个新注册的用户
def InsertRegisterUser(phoneNum, password, nick, sex, idCard,now):
    Config.gdb.insert(
        "user",
        userid = int(phoneNum),
        password = password,
        secpassword = Config.DEFAULT_SECPASSWORD,
        nick = nick,
        phonenum = phoneNum,
        sex = sex,
        idcard = idCard,
        status = Config.USER_STATUS_NOLMAL,
        createtime = now,
        lastlogintime = now,
    )