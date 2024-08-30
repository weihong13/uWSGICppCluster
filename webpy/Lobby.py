#-*- encoding:utf-8 -*-

import Config
import ShopCfg
import datetime

# 通用的一些方法

# 获取用户的金币数量
def getMoney(userId,paytype):
    # 获取缓存中的键
    strKey = Config.KEY_PACKAGE.format(userid=userId)
    money = 0
    # 判断缓存中是否存在该键值
    if Config.grds.exists(strKey):
        money = int(Config.grds.hget(strKey,paytype))
    # 缓存没有，去数据库取出
    else:
        # 获取数据库中的背包信息
        result = Config.gdb.select('package',what = '*',where="userid=$userid",vars=dict(userid=userId))
        if result:
            packageInfo = {
                'bond':result[0]['bond'],
                'coin':result[0]['coin'],
                'prop_1001':result[0]['prop_1001'],
                'prop_1002':result[0]['prop_1002'],
                'prop_1003':result[0]['prop_1003'],
                'prop_1004':result[0]['prop_1004'],
                'prop_1005':result[0]['prop_1005'],
                'freshtime':result[0]['freshtime'],
            }
            # 更新缓存信息
            Config.grds.hmset(strKey,packageInfo)
            # 设置过期时间，一个月
            Config.grds.expire(strKey,30*24*60*60)
            money = int(result[0][paytype])

    return money

def getInventory(pid):
    # 获取缓存中的键
    strKey = Config.KEY_SHOP_CFG_INVENTORY.format(pid=pid)
    inventory = 0
    if Config.grds.exists(strKey):
        inventory = int(Config.grds.hget(strKey,'inventory'))
    else:
        inventory = int(ShopCfg.SHOP_CFG[pid]['inventory'])
        num = {
            'inventory':inventory,
        }
        Config.grds.hmset(strKey,num)
        Config.grds.expire(strKey,24*60*60)
    
    return inventory

# 获取本周周一日期
def getMonday(today):
    today = datetime.datetime.strptime(str(today),"%Y_%m_%d")
    monday = today - datetime.timedelta(today.weekday())
    return datetime.datetime.strftime(monday, "%Y_%m_%d")

