#-*- encoding:utf-8 -*-

import ShopCfg
import ErrorCfg
import math
import Config
import Lobby
import DBManage
import datetime

# 关于商城的方法


# 获取商城配置
def getShopCfg(version):
    # 获取要展示商品id列表
    shopIdList = ShopCfg.SHOP_LIST
    # 商品列表
    shopList = []

    # 遍历商品id列表
    for id in shopIdList:
        # 如果商品id在商城配置中
        if id in ShopCfg.SHOP_CFG:
            # 获取商品
            cfg = ShopCfg.SHOP_CFG[id]
            # 判断客户端版本号与商品版本
            if version < cfg['version']:
                # 客户端版本小于商品版本，跳过
                continue
            # 获取商品属性
            product = {
                "pid":cfg['pid'], "name":cfg['name'],
                "type":cfg['type'],"bond":cfg['bond'], "coin":cfg['coin'], 
                "paytype":cfg['paytype'], "iconid":cfg['iconid'], "version":cfg['version'],
                "discount":cfg['discount'], "inventory":cfg['inventory'], "buylimittype":cfg['buylimittype'], 
                "buylimitnum":cfg['buylimitnum'], "porplist":cfg['porplist'],
            }
            shopList.append(product)
    return {'shopList':shopList,'shopversion':ShopCfg.SHOP_VERSION}



# 商品购买
def shopBuy(userId, propId, buyNum, shopVersion, version):
    # 判断商城版本号
    if shopVersion < ShopCfg.SHOP_VERSION:
        return {'code':ErrorCfg.EC_SHOP_VERSION_LOW, 'reason':ErrorCfg.ER_SHOP_VERSION_LOW}
    # 判断该商品是否上架
    if propId not in ShopCfg.SHOP_LIST:
        return {'code':ErrorCfg.EC_PROP_NOT_SHOW, 'reason':ErrorCfg.ER_PROP_NOT_SHOW}
    # 判断该商品是否存在
    if propId not in ShopCfg.SHOP_CFG:
        return {'code':ErrorCfg.EC_PROP_NOT_EXIST, 'reason':ErrorCfg.ER_PROP_NOT_EXIST}

    cfg = ShopCfg.SHOP_CFG[propId]
    # 判断购买商品的版本号
    if version < cfg['version']:
        return {'code':ErrorCfg.EC_PROP_VERSION_LOW, 'reason':ErrorCfg.ER_PROP_VERSION_LOW}

    # 判断限购数量
    if buyNum > cfg['buylimitnum']:
        return {'code':ErrorCfg.EC_PROP_BUY_LIMIT, 'reason':ErrorCfg.ER_PROP_BUY_LIMIT}
    
    # 判断库存数量
    # ！！！！！ 去缓存或数据库 取出剩余库存，（后续需要修改）！！！！！
    # 修改后
    inventory = 0
    # 获得当前库存
    inventory = Lobby.getInventory(propId)
    if buyNum > inventory:
        return {'code':ErrorCfg.EC_INVENTORY_NOT_ENOUGH, 'reason':ErrorCfg.ER_INVENTORY_NOT_ENOUGH}
    
    # 购买
    # 获取用余额、扣钱等操作（后续完善）
    # 在扣钱的时候，需要考虑数据一致性的问题
    # 计算折扣完的实际计算金额
    paytype = ''
    if cfg['paytype'] == ShopCfg.PAY_TYPE_COIN:
        paytype = 'coin'
        needMoney = int(math.floor(cfg['coin'] * cfg['discount'] * buyNum))
        money = Lobby.getMoney(userId,paytype)
    elif cfg['paytype'] == ShopCfg.PAY_TYPE_BOND:
        paytype = 'bond'
        needMoney = int(math.floor(cfg['bond'] * cfg['discount'] * buyNum))
        money = Lobby.getMoney(userId,paytype)
    
    # 判断余额是否足够
    if money < needMoney:
        return {'code':ErrorCfg.EC_SHOP_BUY_MONEY_NOT_ENOUGH, 'reason':ErrorCfg.ER_SHOP_BUY_MONEY_NOT_ENOUGH}

    # 修改金额
    result = modifyMoney(userId, paytype, -needMoney)
    if result['code'] != 0:
        return {'code':ErrorCfg.EC_SHOP_BUY_MONEY_NOT_ENOUGH, 'reason':ErrorCfg.ER_SHOP_BUY_MONEY_NOT_ENOUGH}
    
    money = result['money']
    
    # 减少库存
    # 获取商品库存的键值
    strKey = Config.KEY_SHOP_CFG_INVENTORY.format(pid=propId)
    # 有其他操作导致库存减少，库存不够了
    if inventory < buyNum:
        # 把金币加回去
        Config.grds.hincrby(strKey,paytype,+needMoney)
        return {'code':ErrorCfg.EC_INVENTORY_NOT_ENOUGH, 'reason':ErrorCfg.ER_INVENTORY_NOT_ENOUGH}
    # 计算最新的库存
    inventory = Config.grds.hincrby(strKey, 'inventory', -buyNum)
    # 有其他操作导致库存减少，库存不够了
    if inventory < 0:
        # 进行退回操作
        inventory = Config.grds.hincrby(strKey, 'inventory', +buyNum)
        # 把金币加回去
        Config.grds.hincrby(strKey,paytype,+needMoney)
        return {'code':ErrorCfg.EC_INVENTORY_NOT_ENOUGH, 'reason':ErrorCfg.ER_INVENTORY_NOT_ENOUGH}
    # 更新新的库存
    # ！！！ 这一步线程是不安全的！！！！后续需要进行改进，
    # 如果将商城配置存入缓存的话，就是安全的，后续使用脚本更新商城配置
    ShopCfg.SHOP_CFG[propId]['inventory'] = inventory

    # 发货
    sendGoods(userId, propId, buyNum)

    return {'code':0, paytype:money}


# 发奖励

# 修改金额
def modifyMoney(userId, paytype, money):
    now = datetime.datetime.now()
    strKey = Config.KEY_PACKAGE.format(userid = userId)
    # 计算剩余的金币或者点券
    modifiedMoney = Config.grds.hincrby(strKey,paytype,money)
    # 如果剩余的金钱小于0了，说明在这个购买操作之间，有其他的操作修改了金币价格，则需要退回
    if modifiedMoney < 0:
        # 把金币退回到修改之前
        Config.grds.hincrby(strKey,paytype,-money)
        # 返回错误
        return {'code':ErrorCfg.EC_MONEY_NOT_ENOUGH, 'reason':ErrorCfg.ER_MONEY_NOT_ENOUGH}

    DBManage.updateMoney(userId, paytype, modifiedMoney, now)
    return {'code':0, 'money':modifiedMoney}


# 发货--发送道具
def sendGoods(userId, propId, propNum):
    strKey = Config.KEY_PACKAGE.format(userid=userId)
    propList = ShopCfg.SHOP_CFG[propId]['porplist']
    now = datetime.datetime.now()
    propDict = {}

    for prop in propList:
        propid = "prop_"+str(prop['id'])
        print(propid)
        print(prop['num'])
        singlePropNum = Config.grds.hincrby(strKey, propid, (prop['num']*propNum))
        propDict[propid] = singlePropNum
    

    Config.grds.hset(strKey,'freshtime',str(now))
    DBManage.updatePackage(userId, propDict, now)
