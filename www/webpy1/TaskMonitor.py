#-*- encoding:utf-8 -*-


from proto.massage_pb2 import Message
from proto.general_pb2 import Sign
import ActionCfg
import Config
import MessageCfg
import TaskCfg
import ErrorCfg
import datetime
import Task

# 处理任务的脚本


    
def TaskMonitor():
    while True:
        strKey = ActionCfg.KEY_ACTION_TASK_LIST
        # 从消息队列中弹出消息
        res = Config.grds.blpop(strKey)[1]
        msg = Message()
        # 反序列化
        msg.ParseFromString(res)

         # 根据事件分发配置，发送数据
        msgId = int(msg.msgid) & MessageCfg.MSGID
        if msgId == MessageCfg.MSGID_SIGN:
            signInfo = Sign()
            signInfo.ParseFromString(msg.string)
            userId = int(signInfo.userid)
            signType = int(signInfo.signtype)
            date = signInfo.date
            
            for id in TaskCfg.TASK_LIST:
                if id not in TaskCfg.TASK_CFG:
                    return {'code':ErrorCfg.EC_TASK_NOT_EXIST, 'reason':ErrorCfg.ER_TASK_NOT_EXIST}
                else:
                    cfg = TaskCfg.TASK_CFG[id]
                    if cfg['action'] != ActionCfg.ACTION_SIGN:
                        continue
                    today = datetime.datetime.strptime(str(date),"%Y_%m_%d")
                    strDate = Task.getTaskStrDate(cfg['type'], today) # 转为字符串格式，这里日期会变
                    strKey = Config.KEY_TASK.format(userid=userId, date=strDate)
                    # 判断key是否存在，不存在，需要初始化
                    if not Config.grds.exists(strKey):
                        Task.initTaskCfg(userId, strDate, cfg['type'])
                    # 获取字段名
                    countField = 'count_' + str(id)
                    totalField = 'total_' + str(id)
                    stateField = 'state_' + str(id)
                    # 修改已完成数量
                    count = Config.grds.hincrby(strKey, countField, 1)
                    print("count {}".format(count))
                    # 获取状态、目标值
                    result = Config.grds.hmget(strKey, stateField, totalField)
                    state = int(result[0])
                    total = int(result[1])

                    # 判断是否已经领取过奖励
                    if state == TaskCfg.STATE_AWARDED:
                        Config.grds.hincrby(strKey, countField, -1)
                        continue
                    # 判断是否有效
                    if state == TaskCfg.STATE_INVALID:
                        Config.grds.hincrby(strKey, countField, -1)
                        continue
                    # 判断任务是否完成
                    if count >= total and state== TaskCfg.STATE_NOT_FINISH:
                        # 修改任务状态为已完成
                        Config.grds.hset(strKey, stateField, TaskCfg.STATE_FINISH)
                        # 通知客户端
             
        elif msgId == MessageCfg.MSGID_LOGIN:
           
           pass


if __name__ == "__main__":
    TaskMonitor()