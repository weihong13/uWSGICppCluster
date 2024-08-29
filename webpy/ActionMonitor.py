#-*- encoding:utf-8 -*-

import ActionCfg
import Config
from proto.massage_pb2 import Message
import MessageCfg

# 分发事件的脚本


# 
def DistributeAction(actionType, actionMsg):
    for key in ActionCfg.ACTION_MAPPING[actionType]:
        Config.grds.rpush(key, actionMsg)
    

def ActionMonitor():
    while True:
        
        strKey = ActionCfg.KEY_ACTION_LIST
        print("ActionMonitor strKey {}".format(strKey))
        # 从消息队列中弹出消息
        res = Config.grds.blpop(strKey)[1]
        msg = Message()
        # 反序列化
        msg.ParseFromString(res)

        # 根据事件分发配置，发送数据
        msgId = int(msg.msgid) & MessageCfg.MSGID
        if msgId == MessageCfg.MSGID_SIGN:
            print("ActionMonitor MSGID_SIGN")
            DistributeAction(ActionCfg.ACTION_SIGN, res)
        elif msgId == MessageCfg.MSGID_LOGIN:
            DistributeAction(ActionCfg.ACTION_LOGIN, res)
                
if __name__ == "__main__":
    ActionMonitor()