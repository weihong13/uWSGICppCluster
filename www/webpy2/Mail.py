#-*- encoding:utf-8 -*-

# 发送邮件
import json
import Config
import ErrorCfg
import Shop
import ShopCfg
from proto.general_pb2 import Mail
from proto.massage_pb2 import Message
import Service


def sendMail(mailInfo):
    # 判断邮件信息
    if not mailInfo:
        return {'code':ErrorCfg.EC_MAIL_INFO_ERROR, 'reason':ErrorCfg.ER_MAIL_INFO_ERROR}
    # 构建邮件的proto
    mailProto = Mail()
    # 存储转发的userid列表
    for userId in mailInfo['useridlist']:
        mailProto.userid.append(userId)

    #  type = '', title = '', context = '', attach = '', fromuserid = '', isglobal = ''
    # 存储其他字段
    mailProto.type = mailInfo['type']
    mailProto.title = mailInfo['title']
    mailProto.context = mailInfo['context']
    mailProto.fromuserid = mailInfo['fromuserid']
    
    # 校验附件，是否为json格式
    # mailProto.attach = json.loads(mailProto.attach)
    # 附件信息
    attach = {}
    for propid,propnum in mailInfo['attach'].items():
        # 判断该商品是否存在
        if propid in ShopCfg.SHOP_CFG:
           attach[propid] = propnum

    mailProto.attach = json.dumps(attach)
    # 附件的一些属性
    mailProto['hasattach']  = 0
    mailProto['getattach']  = 0
    if attach:
        mailProto['hasattach']  = 1

    # # 使用message.proto封装 mail.proto
    # # 然后发送msg即可
    # msgProto = Message()
    # msgProto.userid = userId
    # msgProto.msgid = xxx
    # mailProto.string = mailProto.SerializeToString()



    # 发送给邮件服务器--填入邮件服务器的ip和地址
    Service.sendSvrd('ip','port',mailProto.SerializeToString())
    return {'code':0 }

# 获取全服邮件
def getGlobalMail(userId):
    # 判断用户的登录时间

    # 获取该用户登录时间之前 未过期的全服邮件

    # 一直在线的用户提供脚本，直接给当前在线的用户发送

    # 返回全服邮件
    pass

# 获取邮件列表
def getMailList(userId):

    # 获取全服邮件
    # 当用户登录时，才去拉取全服的邮件
    getGlobalMail(userId)

    # 邮件列表的key
    strKeyList = Config.KEY_MAIL_LIST.format(userid=userId)
    # 从邮件列表的缓存中，取出所有的邮件id
    mailIdList =  Config.grds.lrange(strKeyList, 0, -1)
    # 存储邮件信息的列表
    mailInfoList = []
    # 根据邮件id挨个取出邮件的具体信息
    for mailId in mailIdList:
        # 每个邮件的key
        strKey = Config.KEY_MAIL_DETAIL.format(mailid=mailId)
        # 如果单个邮件的缓存已过期，直接跳过
        # 也可以将在过期之前，将邮件存放到数据库中，做持久化保存。
        # 缓存读不到就去数据库读
        if not Config.grds.exists(strKey):
            Config.grds.lrem(strKeyList, mailId, 0)
            continue
        # 获取邮件的详细内容
        result = Config.grds.hgetall(strKey) 
        mailInfo = {}
        mailInfo['mailid'] = mailId
        mailInfo['title'] = result['title']
        mailInfo['type'] = result['type']
        mailInfo['fromuserid'] = result['fromuserid']
        mailInfo['hasattach'] = result['hasattach']
        # 将邮件添加到邮件信息列表中
        mailInfoList.append(mailInfo)
    
    return mailInfoList

# 获取邮件内容
def getMailDetail(userId):
    # 邮件列表的key
    strKeyList = Config.KEY_MAIL_LIST.format(userid=userId)
    # 从邮件列表的缓存中，取出所有的邮件id
    mailIdList =  Config.grds.lrange(strKeyList, 0, -1)
    # 存储邮件信息的列表
    mailInfoList = []
    # 根据邮件id挨个取出邮件的具体信息
    for mailId in mailIdList:
        # 每个邮件的key
        strKey = Config.KEY_MAIL_DETAIL.format(mailid=mailId)
        # 如果单个邮件的缓存已过期，直接跳过
        # 也可以将在过期之前，将邮件存放到数据库中，做持久化保存。
        # 缓存读不到就去数据库读
        if not Config.grds.exists(strKey):
            Config.grds.lrem(strKeyList, mailId, 0)
            continue
        # 获取邮件的详细内容
        result = Config.grds.hgetall(strKey) 
        mailInfo = {}
        mailInfo['mailid'] = mailId
        mailInfo['type'] = result['type']
        mailInfo['title'] = result['title']
        mailInfo['fromuserid'] = result['fromuserid']
        mailInfo['hasattach'] = result['hasattach']
       
        # 邮件内容
        mailInfo['attach'] = result['attach']
        mailInfo['context'] = result['context']
        mailInfo['getattach'] = result['getattach']
        # 将邮件添加到邮件信息列表中
        mailInfoList.append(mailInfo)
    
    return mailInfoList


# 删除邮件
def deleteMail(userId, mailId):
    # 邮件列表的key
    strKeyList = Config.KEY_MAIL_LIST.format(userid=userId)
    # 删除邮件列表中的邮件id
    Config.grds.lrem(strKeyList, mailId, 0)
    # 邮件的key
    strKey = Config.KEY_MAIL_DETAIL.format(mailid=mailId)
    # 删除邮件内容
    Config.grds.delete(strKey)

    return {'code':0 }


# 获取附件奖励
def getMailAttach(userId, mailId):
    # 邮件列表的key
    strKeyList = Config.KEY_MAIL_LIST.format(userid=userId)
    # 邮件的key
    strKey = Config.KEY_MAIL_DETAIL.format(mailid=mailId)
    # 判断邮件是否存在
    if not Config.grds.exists(strKey):
        Config.grds.lrem(strKeyList, mailId, 0)
        return {'code':ErrorCfg.EC_MAIL_NOT_EXIST, 'reason':ErrorCfg.ER_MAIL_NOT_EXIST}
    
    # 获取邮件的详细内容
    result = Config.grds.hgetall(strKey) 

    attach = {}
    # 附件内容
    attach['attach'] = result['attach']
    # 道具信息
    propInfo = {}
    # 附件类别
    attachList = []
    # 挨个出去道具信息
    for propid,propnum in attach['attach'].items():
        # 判断该商品是否存在，不存在直接跳过
        if propid not in ShopCfg.SHOP_CFG:
           continue
        propInfo[propid] = propnum
        attachList.append(propInfo)
    
    # 发送道具
    for reward in attachList:
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
    # 返回附件道具列表
    return {'code':0 ,'attachList':attachList}


def deleteAllMail(userId):
    # 邮件列表的key
    strKeyList = Config.KEY_MAIL_LIST.format(userid=userId)
    # 从邮件列表的缓存中，取出所有的邮件id
    mailIdList =  Config.grds.lrange(strKeyList, 0, -1)


    # 循环删除每一条数据
    # 应该是删除已读，并且以领取奖励的邮件
    # 需要添加判断
    for mailId in mailIdList:
        # 删除邮件列表中的数据
        Config.grds.lrem(strKeyList, mailId, 0)
        # 每个邮件的key
        strKey = Config.KEY_MAIL_DETAIL.format(mailid=mailId)
        # 删除邮件内容
        Config.grds.delete(strKey)
    
    return {'code':0}