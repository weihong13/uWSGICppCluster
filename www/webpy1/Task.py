#-*- encoding:utf-8 -*-

import ErrorCfg
import TaskCfg
import Config
import datetime # type: ignore
import json
import Lobby
import ShopCfg
import Shop
from proto.general_pb2 import Sign
import Action
import MessageCfg

# 关于任务的方法


# 初始化任务配置
def initTaskCfg(userId, strDate, tasktype = TaskCfg.TYPE_DAY):
    taskInfo = {}
    strKey = Config.KEY_TASK.format(userid=userId, date=strDate)
    # 遍历任务id列表
    for id in TaskCfg.TASK_LIST:
        # 如果任务id在任务配置中
        if id in TaskCfg.TASK_CFG:
            # 获取任务
            cfg = TaskCfg.TASK_CFG[id]
            if tasktype == TaskCfg.TYPE_WEEK:
                if cfg['type'] == tasktype:
                    # 添加任务当前完成的进度
                    taskInfo['count_'+str(id)] = 0 
                    # 添加任务完成的目标
                    taskInfo['total_'+str(id)] = cfg['total']
                    # 任务状态
                    taskInfo['state_'+str(id)] = TaskCfg.STATE_NOT_FINISH
                    # 记录任务奖励，防止任务配置变化
                    taskInfo['reward_'+str(id)] = json.dumps(cfg['rewardlist'])
            elif tasktype == TaskCfg.TYPE_MONTH:
                 if cfg['type'] == tasktype:
                    # 添加任务当前完成的进度
                    taskInfo['count_'+str(id)] = 0
                    # 添加任务完成的目标
                    taskInfo['total_'+str(id)] = cfg['total']
                    # 任务状态
                    taskInfo['state_'+str(id)] = TaskCfg.STATE_NOT_FINISH
                    # 记录任务奖励，防止任务配置变化
                    taskInfo['reward_'+str(id)] = json.dumps(cfg['rewardlist'])
            elif tasktype == TaskCfg.TYPE_YEAR:
                 if cfg['type'] == tasktype:
                    # 添加任务当前完成的进度
                    taskInfo['count_'+str(id)] = 0
                    # 添加任务完成的目标
                    taskInfo['total_'+str(id)] = cfg['total']
                    # 任务状态
                    taskInfo['state_'+str(id)] = TaskCfg.STATE_NOT_FINISH
                    # 记录任务奖励，防止任务配置变化
                    taskInfo['reward_'+str(id)] = json.dumps(cfg['rewardlist'])
            else:
                # 添加任务当前完成的进度
                taskInfo['count_'+str(id)] = 0
                # 添加任务完成的目标
                taskInfo['total_'+str(id)] = cfg['total']
                # 任务状态
                taskInfo['state_'+str(id)] = TaskCfg.STATE_NOT_FINISH
                # 记录任务奖励，防止任务配置变化
                taskInfo['reward_'+str(id)] = json.dumps(cfg['rewardlist'])
    Config.grds.hset(strKey, mapping=taskInfo)


def getTaskStrDate(type, today):
    # 按照任务类型，改变key
    if type == TaskCfg.TYPE_WEEK:
        strDate = Lobby.getMonday(today)
    elif type == TaskCfg.TYPE_MONTH:
        strDate = str(today.year) + "_" + str(today.month) + "_1"
    elif type == TaskCfg.TYPE_YEAR:
        strDate = str(today.year) + "_1_1"
    else:
        strDate = today

    return strDate




# 获取任务配置
def getTaskCfg(userId,version):
    # 获取要展示任务id列表
    taskIdList = TaskCfg.TASK_LIST
    # 任务列表
    taskList = []
    
    now = datetime.datetime.now()
    strDate = now.strftime("%Y_%m_%d")
    strKey = Config.KEY_TASK.format(userid=userId, date=strDate)
    # 判断缓存中是否已经有任务配置了，没有的话，需要初始化任务
    if not Config.grds.exists(strKey):
        initTaskCfg(userId, strDate)

    # 遍历任务id列表
    for id in taskIdList:
        # 如果任务id在任务配置中
        if id in TaskCfg.TASK_CFG:
            # 获取任务
            cfg = TaskCfg.TASK_CFG[id]
            # 判断客户端版本号与任务版本
            if version < cfg['version']:
                # 客户端版本小于任务版本，跳过
                continue
            # 获取任务属性
            taskDict = {
                'tid':cfg['tid'], 'name':cfg['name'],'type':cfg['type'], 
                'iconid':cfg['iconid'], 'series':cfg['series'],"desc":cfg['desc'], 
                'total':cfg['total'], 'version':cfg['version'], 'rewardlist':cfg['rewardlist'],
                'count':0,
            }
            strKey = Config.KEY_TASK.format(userid=userId, date=now.strftime("%Y_%m_%d"))

            strDate = getTaskStrDate(cfg['type'], strDate)
            
            strKey = Config.KEY_TASK.format(userid=userId, date=strDate)
            if not Config.grds.exists(strKey):
                initTaskCfg(userId, strDate, cfg['type'])
            taskInfo = Config.grds.hgetall(strKey)
            if taskInfo:
                countField = 'count_' + str(id)
                stateField = 'state_' + str(id)
                taskDict['count'] = taskInfo[countField] if countField in taskInfo else 0
                taskDict['state'] = taskInfo[stateField] if stateField in taskInfo else TaskCfg.STATE_INVALID
            taskList.append(taskDict)
    return {'taskList':taskList}


# 领取任务奖励
def taskReward(userId, taskId):
    # 判断任务是否存在
    if taskId not in TaskCfg.TASK_LIST:
        return {'code':ErrorCfg.EC_TASK_NOT_EXIST, 'reason':ErrorCfg.ER_TASK_NOT_EXIST}
    
    # 获取任务
    cfg = TaskCfg.TASK_CFG[taskId]

    # 判断用户任务是否完成
    now = datetime.datetime.now()
    strDate = now.strftime("%Y_%m_%d")
    strDate = getTaskStrDate(cfg['type'], strDate)

    strKey = Config.KEY_TASK.format(userid=userId, date=strDate)
    # 判断缓存中是否已经有任务配置了，没有的话，需要初始化任务
    if not Config.grds.exists(strKey):
        initTaskCfg(userId, strDate)

    stateField = 'state_' + str(taskId)
    state = Config.grds.hget(strKey, stateField)
    # 判断任务状态是否完成
    if int(state) == TaskCfg.STATE_NOT_FINISH:
        return {'code':ErrorCfg.EC_TASK_NOT_FINISH, 'reason':ErrorCfg.ER_TASK_NOT_FINISH} 
    # 判断任务是否有效
    if int(state) == TaskCfg.STATE_INVALID:
        return {'code':ErrorCfg.EC_TASK_STATE_INVALID, 'reason':ErrorCfg.ER_TASK_STATE_INVALID} 
    # 判断任务是否已经领取奖励了
    if int(state) == TaskCfg.STATE_AWARDED:
        return {'code':ErrorCfg.EC_TASK_STATE_AWARDED, 'reason':ErrorCfg.ER_TASK_STATE_AWARDED} 
    
    # 发送奖励
    rewardList = TaskCfg.TASK_CFG[taskId]['rewardlist']
    for reward in rewardList:
        rewardId = reward['id']
        rewardNum = reward['num']
        # 发送金钱
        if rewardId == ShopCfg.ID_COIN or rewardId == ShopCfg.ID_BOND:
            result = Shop.modifyMoney(userId, ShopCfg.SHOP_CFG[rewardId]['type'], rewardNum)
            if result['code'] != 0:
                return {'code':ErrorCfg.EC_TASK_CLAIM_FAILED, 'reason':ErrorCfg.ER_TASK_CLAIM_FAILED} 
        else:
            # 发送道具
            Shop.sendGoods(userId, rewardId, rewardNum)
    # 修改任务状态为已领取
    Config.grds.hset(strKey, stateField, TaskCfg.STATE_AWARDED)


    return {'code':0}

# 用户签到
def userSign(userId, signType, date):
    # 判断签到类型
    if signType == TaskCfg.SIGN_TYPE_TODAY:
        date = datetime.datetime.today()
    elif signType == TaskCfg.SIGN_TYPE_AGO:
        date = datetime.datetime.strptime(str(date), "%Y_%m_%d")
    else:
        return {'code':ErrorCfg.EC_TASK_SIGN_TYPE_ERROR, 'reason':ErrorCfg.ER_TASK_SIGN_TYPE_ERROR}
    
    # 判断这一天是否已经签到 
    
    
    day = date.day
    month_firstday = str(date.year) + "_" + str(date.month) + "_1"
    # 签到
    strKey = Config.KEY_SIGN.format(userid=userId, date=month_firstday)
    # 设置位图
    Config.grds.setbit(strKey, day, 1)
    
    # 发送签到事件
    signProto = Sign()
    signProto.userid = userId
    signProto.signtype = signType
    signProto.date = date.strftime("%Y_%m_%d")
    Action.sendAction(userId, MessageCfg.MSGID_SIGN, signProto.SerializeToString())

    return {'code':0}