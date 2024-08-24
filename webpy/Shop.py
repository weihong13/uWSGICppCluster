#-*- encoding:utf-8 -*-

import ShopCfg
import ErrorCfg

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
    if buyNum > cfg['inventory']:
        return {'code':ErrorCfg.EC_INVENTORY_NOT_ENOUGH, 'reason':ErrorCfg.ER_INVENTORY_NOT_ENOUGH}
    
    # 购买
    # 获取用余额、扣钱等操作（后续完善）
    
    # 发货
    return {'code':0}