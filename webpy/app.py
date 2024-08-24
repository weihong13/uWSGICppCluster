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

urls = (
    '/','hello',
    '/register','Register',
    '/login','Login',
    '/shop/cfg','ShopCfg',
    '/shop/buy','ShopBuy',
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

class ShopCfg:
    @catchError
    @checkhLogin
    def GET(self):
        req = web.input(version = '')
        version = int(req.version)
        
        # 获取商城配置
        shopCfg = Shop.getShopCfg(version)

        return json.dumps({'code':0,'shopcfg':shopCfg})

class ShopBuy:
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

# if __name__ == '__main__':
#     # app.run()
    
   