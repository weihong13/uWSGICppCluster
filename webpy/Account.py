#-*- encoding:utf-8 -*-

import AccountCfg
import re
import Config
import datetime
import DBManage
import ErrorCfg

# 账号相关的函数

# 检测手机号格式
def checkPhoneNum(phoneNum):
    # 1、使用号段列表进行判断
    phoneList = [139,138,137,136,134,135,147,150,151,152,157,158,159,172,178,
                 130,131,132,140,145,146,155,156,166,185,186,175,176,196,
                 133,149,153,177,173,180,181,189,191,193,199,
                 162,165,167,170,171]
    
    # 2、使用正则表达式判断
    if len(phoneNum) == 11 and str(phoneNum).isdigit() and (int(phoneNum[:3]) in phoneList):
        return True
    else:
        return False


# 检验账号是否重复
def checkUserIdNotRepeat(userId):
    # 检测账号是否重复，重复返回false 不重复返回true
    result = Config.gdb.select("user",where = "userid=$userid",vars=dict(userid=userId),what='count(*) as num')
    # 等于这个
    # ret = Config.gdb.query("select count(*) as num from user where userid = {}".format(userId))
    
    # 取到查询结果的第一行的num字段
    if result and result[0].num >= 1:
        return False
    return True

# 检测身份证号是否正确
def checkIdCard(idCard):  
    strIdCard = str(idCard).strip()  
    if not strIdCard.isdigit() and (len(strIdCard) != 15 and len(strIdCard) != 18):
        return False  
  
    # 地区检验  
    if strIdCard[:2] not in AccountCfg.AREAID:
        return False  
  
    # 15位身份证号码检测  
    if len(strIdCard) == 15:  
        # 闰年合法性检测（15位身份证基于出生年份的后两位）  
        birth_year = int(strIdCard[6:8]) + 1900  
        if (birth_year % 400 == 0) or (birth_year % 100 != 0 and birth_year % 4 == 0):  
            pattern = re.compile(
                r'[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  
        else:  
            pattern = re.compile(  
                r'[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  
        if re.match(pattern, strIdCard):  
            return True  
        else:
            return False  
  
    # 18位身份证号码检测  
    elif len(strIdCard) == 18:
        pattern = re.compile(
            r'[1-9][0-9]{5}(18|19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  
        # 出生日期合法性检测
        if re.match(pattern, strIdCard):
            # 计算检验位
            weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            sum = 0
            for i in range(17):
                sum += int(strIdCard[i]) * weights[i]
            check_digit = check_codes[sum % 11]
            if check_digit.upper() == strIdCard[17].upper():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
# 检测密码格式 
def checkPassword(password):
    # 字母、数字和可选字符!@#*?.+，至少一个数字和一个字母，8-16位  
    pattern = re.compile('^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z!@#*?.+]{8,16}$')  
    if re.match(pattern, password): 
        return True  
    return False 


# 注册用户--初始化一个用户
def initUser(phoneNum, password, nick, sex, idCard):
    now = datetime.datetime.now()
    DBManage.insertRegisterUser(phoneNum, password, nick, sex, idCard,now)
    # 初始化用户背包
    strKey = Config.KEY_PACKAGE.format(userid = phoneNum)
    packageInfo = {
        'bond':0,
        'coin':Config.NEWUSER_DEFAULT_COIN,
        'prop_1001':0,
        'prop_1002':0,
        'prop_1003':0,
        'prop_1004':0,
        'prop_1005':0,
        'freshtime':str(now),
    }
    # 将用户的背包信息放入缓存中。
    # 还需要设置缓存中用户背包信息的过期时间，设一个月。不然，一直占用缓存
    # 但是要在登录之后，重新设置背包信息的过期时间
    Config.grds.hmset(strKey,packageInfo)
    Config.grds.expire(strKey,30*24*60*60)

    packageInfo['userid'] = phoneNum
    DBManage.initPackage(packageInfo)


# 校验账户
def verifyAccount(userId, password):
    if not str(userId).isdigit():
         return {'code':ErrorCfg.EC_LOGIN_USERID_ERROR,'reason':ErrorCfg.ER_LOGIN_USERID_ERROR}
    
    # 按照账号直接取出密码，后面可以直接按照密码进行校验，可以少一次数据库查找

    print(userId)
    result = Config.gdb.select("user",what='password',where = "userid=$userid",vars=dict(userid=userId))

    # result = Config.gdb.query("select password from user where userid = {}".format(userId))

    # 没查到账号，用户不存在
    if not result:
        return {'code':ErrorCfg.EC_LOGIN_USERID_ERROR,'reason':ErrorCfg.ER_LOGIN_USERID_ERROR}
    # 密码错误
    if result[0]['password'] != password:
        return {'code':ErrorCfg.EC_LOGIN_PASSWORD_ERROR,'reason':ErrorCfg.ER_LOGIN_PASSWORD_ERROR}
    # 取出该账号的状态，如果已冻结的话，返回错误
    result = Config.gdb.select("user",what='status',where = "userid=$userid",vars=dict(userid=userId))
    # 账号已冻结
    if result[0]['status'] == Config.USER_STATUS_FRERZE:
        return {'code':ErrorCfg.EC_LOGIN_STATUS_FRERZE,'reason':ErrorCfg.ER_LOGIN_STATUS_FRERZE}
    return {'code':0}

# 登录处理
def handleLogin(userId, session):
     # 获取当前时间
    now = datetime.datetime.now()
    # 使用session记录登录状态
    session['userid'] = userId

    # 添加一个新的键，为登录的key，设置过期时间，该键值过期之后，就需要重新登录。
    loginInfo = {
        'freshtime':str(now),
    }
    Config.grds.hmset(Config.KEY_LOGINE.format(userid=userId), loginInfo)
    Config.grds.expire(Config.KEY_LOGINE.format(userid=userId), Config.LOGIN_INVALID_TIME)

    # 更新背包信息的过期时间
    Config.grds.expire(Config.KEY_PACKAGE.format(userid = userId),30*24*60*60)
    # 更新登录时间
    DBManage.updateLastLoginTime(userId,now)

    return {'code':0}