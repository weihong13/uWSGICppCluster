#-*- encoding:utf-8 -*-

import ActionCfg
from proto.massage_pb2 import Message
import Config

# 发送事件 
def sendAction(userId, msgId, protoInfo):
    strKey = ActionCfg.KEY_ACTION_LIST
    msg = Message()
    msg.userid = userId
    msg.msgid = msgId
    msg.string = protoInfo
    Config.grds.rpush(strKey, msg.SerializeToString())