#-*- encoding:utf-8 -*-
import web
import Account
import ErrorCfg
import Error
import json

urls = (
    '/','hello',
    '/register','Register',
    '/login','Login',
)

app = web.application(urls,globals())
application = app.wsgifunc()


class hello:
    def GET(self,name):
        if not name:
            name = 'World!'
        return 'Hello' + name

class Register:
    def POST(self):
        req = web.input(password = '', phoneNum = '', nick = '', sex = '', idCard = '')
        password = req.password
        phoneNum = req.phoneNum
        nick = req.nick
        sex = req.sex
        idCard = req.idCard
        # 检验手机格式
        if not Account.CheckPhoneNum(phoneNum):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PHONENUM_TYPE_ERROR,ErrorCfg.ER_REGISTER_PHONENUM_TYPE_ERROR)
        # 检验账号是否重复
        if not Account.CheckUserIdNotRepeat(phoneNum):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_USERID_REPEAT,ErrorCfg.ER_REGISTER_USERID_REPEAT)
        # 检测身份证号是否正确
        if not Account.CheckIdCard(idCard):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_IDCARD_ERROR,ErrorCfg.ER_REGISTER_IDCARD_ERROR)
        # 检测密码格式 
        if not Account.CheckPassword(password):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PWD_TYPE_ERROR,ErrorCfg.ER_REGISTER_PWD_TYPE_ERROR)
        
        # 注册账号
        Account.InitUser(phoneNum, password, nick, sex, idCard)

        return json.dumps({'code':111,'reason':'register OK'})

class Login:
    def POST(self):
        req = web.input(userId = '', password = '')
        userId = req.userId
        password = req.password
        # 获取登录结果
        result = Account.VerifyAccount(userId,password)
        # 登录失败，直接返回结果
        if result['code'] != 0:
            return Error.ErrResult(result['code'],result['reason'])
        # 登录成功，进行下一步处理

        return json.dumps({'code':0})


# if __name__ == '__main__':
#     # app.run()
    
   