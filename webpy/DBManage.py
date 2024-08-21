#-*- encoding:utf-8 -*-

import Config

# 操作数据库的模块

# 插入一个新注册的用户
def insertRegisterUser(phoneNum, password, nick, sex, idCard,now):
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

# 更新用户的最后登录时间
def updateLastLoginTime(userId,now):
    Config.gdb.update(
        "user",
        lastlogintime = now,
        where = "userid=$userid",
        vars = dict(userid=userId)
    )