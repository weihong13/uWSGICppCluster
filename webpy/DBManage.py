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

# 初始化背包信息
def initPackage(packageInfo):
    result = Config.gdb.insert(
        "package",
        **packageInfo
    )

# 更新金钱
def updateMoney(userId, paytype, money, now):
    
    Config.gdb.query("update package set {paytype} = {money}, freshtime = '{now}' where userid = {userid}".format(paytype=paytype, money=money, now=now, userid=userId))

# 更新背包
def updatePackage(userId, propDict, now):
    propStr = ''
    for k,v in propDict.items():
        propStr += str(k) + "=" + str(v) +","
        print(propStr)

    Config.gdb.query("update package set {propstr} freshtime = '{now}' where userid = {userid}".format(propstr = propStr, now = now, userid= userId))