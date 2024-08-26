#-*- encoding:utf-8 -*-

import ErrorCfg
import TaskCfg
import Config
import datetime # type: ignore
import json
import Lobby
import ShopCfg
import Shop

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
            if Config.grds.exists(strKey):
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
    stateField = 'state_' + str(taskId)
    state = Config.grds.hget(strKey, stateField)
    # 判断任务是否完成
    if state != TaskCfg.STATE_FINISH:
        return {'code':ErrorCfg.EC_TASK_NOT_FINISH, 'reason':ErrorCfg.ER_TASK_NOT_FINISH} 
    
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
        
    return {'code':0}