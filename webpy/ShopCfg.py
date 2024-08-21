#-*- encoding:utf-8 -*-

# 商城版本号
SHOP_VERSION = 202408202226

# 商品类型
GOODS_TYPE_CONSUMABLES = 1  # 消耗型
GOODS_TYPE_TIME = 2         # 时间型

# 商品支付方式
PAY_TYPE_ALL = 0   # 所有
PAY_TYPE_BOND = 1 # 点券
PAY_TYPE_COIN = 2 # 金币

# 限购类型
BUY_LINIT_TYPE_INVALID = 0 # 不限购
BUY_LINIT_TYPE_DAY = 1 # 每日限购
BUY_LINIT_TYPE_WEEK = 2 # 每周限购
BUY_LINIT_TYPE_MONTH = 3 # 每月限购
BUY_LINIT_TYPE_YEAR = 4 # 每年限购

# 商品id
ID_EXPCARD_ONCE = 1001 # 双倍经验卡（单场）
ID_COINCARD_ONEC = 1002 # 双倍金币卡（单场）
ID_RENAME_CARD = 1003 # 改名卡
ID_MONTH_VIP_PACKAGE = 1004 # 月度会员礼包
ID_YEAR_VIP_PACKAGE = 1005  # 年度会员礼包
ID_MONTH_VIP = 1006 # 月度会员
ID_YEAR_VIP = 1007  # 年度会员

# 要显示的商品列表
SHOP_LIST = [
    ID_EXPCARD_ONCE,   # 双倍经验卡（单场）
    ID_COINCARD_ONEC,  # 双倍金币卡（单场）
    ID_RENAME_CARD,    # 改名卡
    ID_MONTH_VIP_PACKAGE,  # 月度会员礼包
    ID_YEAR_VIP_PACKAGE,   # 年度会员礼包
]

# 商品配置
SHOP_CFG = {
    ID_EXPCARD_ONCE:{"pid":ID_EXPCARD_ONCE, "name":"双倍经验卡（单场）","type":GOODS_TYPE_CONSUMABLES,"bond":-1, "coin":1000, "paytype":PAY_TYPE_COIN, "iconid":1001, "version":10000, "discount":1, "inventory":3, "buylimittype":BUY_LINIT_TYPE_INVALID, "buylimitnum":2, "porplist":[{"id":ID_EXPCARD_ONCE, "num":1}]},
    
    ID_COINCARD_ONEC:{"pid":ID_COINCARD_ONEC, "name":"双倍金币卡（单场）","type":GOODS_TYPE_CONSUMABLES,"bond":-1, "coin":1000, "paytype":PAY_TYPE_COIN, "iconid":1002, "version":10000, "discount":1, "inventory":-1, "buylimittype":BUY_LINIT_TYPE_INVALID, "buylimitnum":-1, "porplist":[{"id":ID_COINCARD_ONEC, "num":1}]},
    
    ID_RENAME_CARD:{"pid":ID_RENAME_CARD, "name":"改名卡","type":GOODS_TYPE_CONSUMABLES, "bond":1990, "coin":-1, "paytype":PAY_TYPE_BOND, "iconid":1003 , "version":10000, "discount":1, "inventory":-1, "buylimittype":BUY_LINIT_TYPE_INVALID, "buylimitnum":-1, "porplist":[{"id":ID_RENAME_CARD, "num":1}]},
    
    ID_MONTH_VIP_PACKAGE:{"pid":ID_MONTH_VIP_PACKAGE, "name":"月度会员礼包","type":GOODS_TYPE_CONSUMABLES, "bond":1990, "coin":-1, "paytype":PAY_TYPE_BOND, "iconid":1004 , "version":10000, "discount":1, "inventory":-1, "buylimittype":BUY_LINIT_TYPE_INVALID, "buylimitnum":-1, "porplist":[{"id":ID_EXPCARD_ONCE, "num":1},{"id":ID_COINCARD_ONEC, "num":1},{"id":ID_MONTH_VIP, "num":1}]},
    
    ID_YEAR_VIP_PACKAGE:{"pid":ID_YEAR_VIP_PACKAGE, "name":"年度会员礼包","type":GOODS_TYPE_CONSUMABLES, "bond":21890, "coin":-1, "paytype":PAY_TYPE_BOND, "iconid":1005 , "version":10000, "discount":1, "inventory":-1, "buylimittype":BUY_LINIT_TYPE_INVALID, "buylimitnum":-1, "porplist":[{"id":ID_EXPCARD_ONCE, "num":15},{"id":ID_COINCARD_ONEC, "num":15},{"id":ID_YEAR_VIP, "num":1}]},
  

}