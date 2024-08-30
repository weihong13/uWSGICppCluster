#-*- encoding:utf-8 -*-

import web
import Account
import ErrorCfg
import Error
import json
import logging
import logging.config
import Shop
from RedisStore import RedisStore
import Config
import Mail

import Task

urls = (
    '/','hello',
    '/register','Register',
    '/login','Login',
    '/shop/cfg','Shop_Cfg',
    '/shop/buy','Shop_Buy',
    '/task/cfg','Task_Cfg',
    '/task/reward','Task_Reward',
    '/sign','Sign',
    '/mail/send','Mail_Send',
    '/mail/list','Mail_List',
    '/mail/detail','Mail_Detail',
    '/mail/delete','Mail_Delete',
    '/mail/getattach','Mail_GetAttach',
    'mail/delete/all','Mail_Delete_All'
)

app = web.application(urls,globals())
application = app.wsgifunc()

if web.config.get('_session') is None:
    session = web.session.Session(app, RedisStore(Config.grds, Config.SESSION_EXPIRETIME))
    web.config._session = session
else:
    session = web.config._session

# 获取日志库配置
logging.config.fileConfig('logging.conf')
# 获取记录器
logger = logging.getLogger('applog')


# 装饰器--异常捕获
def catchError(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            # 打印详细的报错信息，使用error方法，报错信息更简单
            logger.exception(e)
    return wrapper

# 装饰器--检测登录
def checkhLogin(func):
    def wrapper(*args,**kwargs):
        if session.__dict__.__contains__('userid'):
            return func(*args,**kwargs)
        else:
            return Error.errResult(ErrorCfg.EC_LOGIN_INVALID,ErrorCfg.ER_LOGIN_INVALID)
    return wrapper


class hello:
    def GET(self,name):
        if not name:
            name = 'World!'
        return 'Hello' + name

class Register:
    @catchError
    def POST(self):
        req = web.input(password ='', phonenum ='', nick ='', sex ='', idcard ='')
        password = req.password
        phoneNum = req.phonenum
        nick = req.nick
        sex = req.sex
        idCard = req.idcard
        # 检验手机格式
        if not Account.checkPhoneNum(phoneNum):
            return Error.errResult(ErrorCfg.EC_REGISTER_PHONENUM_TYPE_ERROR,ErrorCfg.ER_REGISTER_PHONENUM_TYPE_ERROR)
        # 检验账号是否重复
        if not Account.checkUserIdNotRepeat(phoneNum):
            return Error.errResult(ErrorCfg.EC_REGISTER_USERID_REPEAT,ErrorCfg.ER_REGISTER_USERID_REPEAT)
        # 检测身份证号是否正确
        if not Account.checkIdCard(idCard):
            return Error.errResult(ErrorCfg.EC_REGISTER_IDCARD_ERROR,ErrorCfg.ER_REGISTER_IDCARD_ERROR)
        # 检测密码格式 
        if not Account.checkPassword(password):
            return Error.errResult(ErrorCfg.EC_REGISTER_PWD_TYPE_ERROR,ErrorCfg.ER_REGISTER_PWD_TYPE_ERROR)
        
        # 注册账号
        Account.initUser(phoneNum, password, nick, sex, idCard)

        return json.dumps({'code':0})

class Login:
    @catchError
    def POST(self):
        req = web.input(userid = '', password = '')
        userId = req.userid
        password = req.password
        # 获取登录结果
        result = Account.verifyAccount(userId,password)
        # 登录失败，直接返回结果
        if result['code'] != 0:
            return Error.errResult(result['code'],result['reason'])
        
        # 登录成功，进行下一步处理
        result = Account.handleLogin(userId, session)
        if result['code'] != 0:
            return Error.errResult(result['code'],result['reason'])
        return json.dumps({'code':0})

class Shop_Cfg:
    @catchError
    @checkhLogin
    def GET(self):
        req = web.input(version = '')
        version = int(req.version)
        
        # 获取商城配置
        shopCfg = Shop.getShopCfg(version)

        return json.dumps({'code':0,'shopcfg':shopCfg})

class Shop_Buy:
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '', propid = '', buynum = '',shopversion = '', version = '')

        userId = req.userid
        propId = int(req.propid)
        buyNum = int(req.buynum)
        shopVersion = int(req.shopversion)
        version = int(req.version)

        buyInfo = Shop.shopBuy(userId, propId, buyNum, shopVersion, version)
        if buyInfo['code'] != 0:
            return Error.errResult(buyInfo['code'],buyInfo['reason'])
        return json.dumps({'code':0})

# 获取任务配置
class Task_Cfg:
    @catchError
    @checkhLogin
    def GET(self):
        req = web.input(userid = '', version = '')
        userId = int(req.userid)
        version = int(req.version)
        
        # 获取商城配置
        taskCfg = Task.getTaskCfg(userId,version)

        return json.dumps({'code':0,'taskcfg':taskCfg})
    

# 获取任务奖励
class Task_Reward:
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '', taskid = '')
        userId = int(req.userid)
        taskId = int(req.taskid)
        print("Task_Reward taskId {}".format(taskId))
        # 领取奖励
        result = Task.taskReward(userId, taskId)

        if result['code'] != 0:
            return Error.errResult(result['code'], result['reason'])


        return json.dumps({'code':0})
    
# 签到
class Sign:
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '', signtype = '', date = '')
        userId = int(req.userid)
        signType = int(req.signtype)
        date = str(req.date)
        print("Sign date {}".format(date))
        result =Task.userSign(userId, signType, date)
        if result['code'] != 0:
            return Error.errResult(result['code'], result['reason'])

        return json.dumps({'code':0})

def Mail_Send():
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(useridlist = '', type = '', title = '', context = '', attach = '', fromuserid = '', isglobal = '')
        # userId = int(req.useridlist)
        # type = int(req.type)
        # title = req.title
        # context = req.context
        req.attach = json.loads(req.attach)
        # fromUserId = int(req.fromuserid)
        # isglobal = req.isglobal

        result = Mail.sendMail(req)
        if result['code'] != 0:
            return Error.errResult(result['code'], result['reason'])

        return json.dumps({'code':0})

def Mail_List():
    @catchError
    @checkhLogin
    def GET(self):
        req = web.input(userid = '')
        userId = int(req.userid)
        mailInfoList = Mail.getMailList(userId)
        
        return json.dumps({'code':0, 'mailInfoList':mailInfoList})

def Mail_Detail():
    @catchError
    @checkhLogin
    def GET(self):
        req = web.input(userid = '')
        userId = int(req.userid)
        mailInfoList = Mail.getMailDetail(userId)
        
        return json.dumps({'code':0, 'mailInfoList':mailInfoList})



def Mail_Delete():
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '', mailid = '')
        userId = int(req.userid)
        mailId = int(req.mailid)
        result = Mail.deleteMail(userId, mailId)
        if result['code'] != 0:
            return Error.errResult(result['code'], result['reason'])

        return json.dumps({'code':0})


def Mail_GetAttach():
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '', mailid = '')
        userId = int(req.userid)
        mailId = int(req.mailid)
        result = Mail.getMailAttach(userId, mailId)
        if result['code'] != 0:
            return Error.errResult(result['code'], result['reason'])

        return json.dumps({'code':0,'attachList':result['attachList']})


def Mail_Delete_All():
    @catchError
    @checkhLogin
    def POST(self):
        req = web.input(userid = '')
        userId = int(req.userid)
        Mail.deleteAllMail(userId)

    return json.dumps({'code':0})
# if __name__ == '__main__':
#     # app.run()
    
   