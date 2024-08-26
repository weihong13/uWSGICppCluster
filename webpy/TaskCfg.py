#-*- encoding:utf-8 -*-

import ShopCfg

# 任务版本号
TASK_VERSION = 202408202226

# 任务id
ID_INVALID = -1 # 无效id
ID_SIGN = 20001 # 签到
ID_SIGN_SEVENDAYS = 20002 # 签到一周

ID_PLAY_SERIES_1 = 20003 # 连续对局 1阶段（3局）
ID_PLAY_SERIES_2 = 20004 # 连续对局 2阶段 (5局)
ID_PLAY_SERIES_3 = 20005 # 连续对局 3阶段 (10局)

# 任务类型
TYPE_DAY = 1
TYPE_WEEK = 2
TYPE_MONTH = 3
TYPE_YEAR = 4

# 任务状态
STATE_INVALID = -1 # 无效
STATE_NOT_FINISH = 1 # 未完成
STATE_FINISH = 2  # 已完成，未领奖励
STATE_AWARDED = 3 # 已领取奖励

# 展示列表
TASK_LIST = [
    ID_SIGN,     # 签到
    ID_SIGN_SEVENDAYS, # 签到一周
    ID_PLAY_SERIES_1, # 连续对局 1阶段（3局）
    ID_PLAY_SERIES_2, # 连续对局 2阶段 (5局)
    ID_PLAY_SERIES_3, # 连续对局 3阶段 (10局)
]


TASK_CFG = {
    
    ID_SIGN:{'tid':ID_SIGN, 'name':"每日签到", 'type':TYPE_DAY, 'iconid':20001, 'series':ID_INVALID, "desc":"每日签到后领取奖励", 'total':1, 'version':10000, 'rewardlist':[{'id':ShopCfg.ID_COIN, 'num':200}]},
    ID_SIGN_SEVENDAYS:{'tid':ID_SIGN_SEVENDAYS, 'name':"每周签到", 'type':TYPE_WEEK, 'iconid':20002, 'series':ID_INVALID, "desc":"连续签到一周后领取奖励", 'total':7, 'version':10000, 'rewardlist':[{'id':ShopCfg.ID_COIN, 'num':1000},{'id':ShopCfg.ID_EXPCARD_ONCE, 'num':2},{"id":ShopCfg.ID_COINCARD_ONEC, "num":2}]},
    ID_PLAY_SERIES_1:{'tid':ID_PLAY_SERIES_1, 'name':"每日对局3场", 'type':TYPE_DAY, 'iconid':20003, 'series':ID_INVALID, "desc":"每日完成3场对局后领取奖励", 'total':3, 'version':10000, 'rewardlist':[{'id':ShopCfg.ID_COIN, 'num':500},{'id':ShopCfg.ID_EXPCARD_ONCE, 'num':1}]},
    ID_PLAY_SERIES_2:{'tid':ID_PLAY_SERIES_2, 'name':"每日对局5场", 'type':TYPE_DAY, 'iconid':20004, 'series':ID_PLAY_SERIES_1, "desc":"每日完成5场对局后领取奖励", 'total':5, 'version':10000, 'rewardlist':[{'id':ShopCfg.ID_COIN, 'num':1000},{'id':ShopCfg.ID_EXPCARD_ONCE, 'num':1},{"id":ShopCfg.ID_COINCARD_ONEC, "num":1}]},
    ID_PLAY_SERIES_3:{'tid':ID_PLAY_SERIES_3, 'name':"每日对局10场", 'type':TYPE_DAY, 'iconid':20005, 'series':ID_PLAY_SERIES_2, "desc":"每日完成10场对局后领取奖励", 'total':10, 'version':10000, 'rewardlist':[{'id':ShopCfg.ID_COIN, 'num':2000},{'id':ShopCfg.ID_EXPCARD_ONCE, 'num':3},{"id":ShopCfg.ID_COINCARD_ONEC, "num":3}]},
}