#-*- encoding:utf-8 -*-
import web
import Account
import json

urls = (
    '/(.*)','hello',
    '/register','Register',
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
        req = web.input(userId = '', password = '', phoneNum = '', nick = '', sex = '', idCard = '')
        userId = req.userId
        password = req.password
        phoneNum = req.phoneNum
        nick = req.nick
        sex = req.sex
        idCard = req.idCard

        # 检验手机格式
        if not Account.checkPhoneNum(phoneNum):
            return json.loads({'code':101,'reasn':'手机号格式错误，请重新输入'})


# if __name__ == '__main__':
#     # app.run()
    
   